from flask import Flask, render_template, jsonify, request
from data import COMPANIES_RECYCLING, COMPANIES_INACTIVE, COMPANIES_WON, LUSHA_NEW, LUSHA_ROLES, HUMAND_PRODUCT, COMPANIES_BOTH
import csv, io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    source = request.args.get("source", "")
    country = request.args.get("country", "")
    industry = request.args.get("industry", "")
    emp_range = request.args.get("employees", "")
    query = request.args.get("q", "").lower()

    def match_emp(emp, ranges_str):
        if not ranges_str: return True
        ranges = ranges_str.split(",")
        for r in ranges:
            r = r.strip()
            if "-" in r:
                lo, hi = r.split("-")
                if int(lo) <= emp <= int(hi): return True
            elif r.endswith("+"):
                if emp >= int(r.replace("+","")): return True
            else:
                if emp >= int(r): return True
        return False

    def match_filters(c):
        if country and c.get("country","") != country: return False
        if industry and c.get("industry","") != industry: return False
        if emp_range and not match_emp(c.get("employees",0), emp_range): return False
        if query and query not in c.get("name","").lower() and query not in c.get("industry","").lower() and query not in c.get("country","").lower(): return False
        return True

    if source == "all":
        merged = []
        # Companies in BOTH (show both badges)
        both_names = {c["name"] for c in COMPANIES_BOTH}
        for c in COMPANIES_BOTH:
            merged.append({**c, "source": "both", "source_label": c.get("deal_stage","HS+Lusha")})
        # HubSpot only (skip those already in BOTH)
        for c in COMPANIES_RECYCLING:
            if c["name"] not in both_names:
                merged.append({**c, "source": "hubspot", "source_label": "Recycling"})
        for c in COMPANIES_INACTIVE:
            if c["name"] not in both_names:
                merged.append({**c, "source": "hubspot", "source_label": "Inactiva +45d"})
        for c in COMPANIES_WON:
            merged.append({**c, "source": "hubspot", "source_label": "Won"})
        # Lusha only (skip those already in BOTH)
        for c in LUSHA_NEW:
            if c["name"] not in both_names:
                merged.append({**c, "source": "lusha", "source_label": "Lusha Nueva"})
        for c in LUSHA_ROLES:
            merged.append({**c, "source": "lusha", "source_label": "Lusha Rol C-Level"})
        return jsonify([c for c in merged if match_filters(c)])
    elif source == "recycling":
        # Only show if last deal is in BDR pipeline AND no newer deal in Customer Journey (AE)
        valid = [c for c in COMPANIES_RECYCLING if not c.get("has_newer_cj_deal", False)]
        return jsonify([c for c in valid if match_filters(c)])
    elif source == "inactive":
        return jsonify([c for c in COMPANIES_INACTIVE if match_filters(c)])
    elif source == "won":
        return jsonify([c for c in COMPANIES_WON if match_filters(c)])
    elif source == "lusha_new":
        return jsonify([c for c in LUSHA_NEW if match_filters(c)])
    elif source == "lusha_roles":
        return jsonify([c for c in LUSHA_ROLES if match_filters(c)])
    return jsonify([])

@app.route("/api/stats")
def get_stats():
    by_industry = {}
    by_country = {}
    for c in COMPANIES_WON:
        by_industry[c["industry"]] = by_industry.get(c["industry"], 0) + 1
        by_country[c["country"]] = by_country.get(c["country"], 0) + 1
    return jsonify({"by_industry": by_industry, "by_country": by_country, "total": len(COMPANIES_WON)})

@app.route("/api/search")
def search():
    q = request.args.get("q", "").lower()
    if not q:
        return jsonify({"answer": "Preguntame lo que necesites sobre empresas, clientes, o el producto de Humand.", "data": []})

    # Product queries
    for key, info in HUMAND_PRODUCT.items():
        if key in q:
            return jsonify({"answer": info, "data": []})

    # Client queries
    if "cliente" in q or "won" in q or "ganado" in q or "cuantos" in q:
        country_match = ""
        industry_match = ""
        for c in ["méxico","colombia","argentina","perú","brasil","uruguay","paraguay","ecuador","españa"]:
            if c in q: country_match = c.title()
        for ind in ["retail","tecnología","salud","banca","manufactura","alimentación","logística","fintech","turismo","construcción","energía","educación","farmacéutica","seguros","automotriz","minería","consultoría"]:
            if ind in q: industry_match = ind.title()

        results = [c for c in COMPANIES_WON if (not country_match or c["country"]==country_match) and (not industry_match or c["industry"]==industry_match)]
        msg = f"Tenemos {len(results)} clientes"
        if country_match: msg += f" en {country_match}"
        if industry_match: msg += f" en {industry_match}"
        return jsonify({"answer": msg + ".", "data": results, "type": "won"})

    # Lusha queries
    if "nueva" in q or "lusha" in q or "virgen" in q or "no est" in q:
        emp_min = 0
        import re
        m = re.search(r'(\d+)\s*empleados', q) or re.search(r'más de\s*(\d+)', q) or re.search(r'mas de\s*(\d+)', q)
        if m: emp_min = int(m.group(1))
        results = [c for c in LUSHA_NEW if c["employees"] >= emp_min]
        return jsonify({"answer": f"Encontré {len(results)} empresas nuevas en Lusha" + (f" con más de {emp_min} empleados" if emp_min else "") + ".", "data": results, "type": "lusha_new"})

    # Recycling
    if "recycling" in q or "retomar" in q:
        return jsonify({"answer": f"Hay {len(COMPANIES_RECYCLING)} empresas en Recycling.", "data": COMPANIES_RECYCLING, "type": "recycling"})

    # Inactive
    if "inactiv" in q or "45" in q:
        return jsonify({"answer": f"Hay {len(COMPANIES_INACTIVE)} empresas con +45 días sin actividad.", "data": COMPANIES_INACTIVE, "type": "inactive"})

    return jsonify({"answer": "No encontré algo específico. Probá con: 'clientes en Retail', 'empresas nuevas con más de 500 empleados', 'qué módulos tiene Humand', o usá los filtros.", "data": []})

@app.route("/api/filters")
def get_filters():
    all_data = COMPANIES_RECYCLING + COMPANIES_INACTIVE + COMPANIES_WON + LUSHA_NEW + LUSHA_ROLES
    countries = sorted(set(c["country"] for c in all_data if c.get("country")))
    industries = sorted(set(c["industry"] for c in all_data if c.get("industry")))
    return jsonify({"countries": countries, "industries": industries})

@app.route("/api/export-csv", methods=["POST"])
def export_csv():
    from flask import Response
    data = request.json.get("companies", [])
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Empresa", "País", "Industria", "Empleados", "Etapa", "Días inactivos", "Fuente"])
    for c in data:
        writer.writerow([c.get("name",""), c.get("country",""), c.get("industry",""), c.get("employees",""), c.get("deal_stage",""), c.get("days_inactive",""), c.get("source_label","")])
    output.seek(0)
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=bdr-lista.csv"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
