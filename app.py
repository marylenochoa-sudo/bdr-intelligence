from flask import Flask, render_template, jsonify, request
from data import COMPANIES_RECYCLING, COMPANIES_INACTIVE, COMPANIES_WON, LUSHA_NEW, LUSHA_ROLES, HUMAND_PRODUCT, COMPANIES_BOTH
import csv, io, json, os

# Claude AI for smart search
try:
    import anthropic
    ai_client = anthropic.Anthropic()
    HAS_AI = True
except Exception:
    HAS_AI = False

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

def _build_data_context():
    """Build a summary of all available data for the AI."""
    recycling_names = [c["name"] + " (" + c["country"] + ", " + c["industry"] + ", " + str(c["employees"]) + " emp, " + str(c.get("days_in_recycling",0)) + "d en recycling)" for c in COMPANIES_RECYCLING if not c.get("has_newer_cj_deal")]
    inactive_names = [c["name"] + " (" + c["country"] + ", " + c["industry"] + ", " + str(c["employees"]) + " emp, " + str(c["days_inactive"]) + "d inactiva)" for c in COMPANIES_INACTIVE]
    won_names = [c["name"] + " (" + c["country"] + ", " + c["industry"] + ", " + str(c["employees"]) + " emp)" for c in COMPANIES_WON]
    lusha_names = [c["name"] + " (" + c["country"] + ", " + c["industry"] + ", " + str(c["employees"]) + " emp)" for c in LUSHA_NEW]
    lusha_roles_names = [c["name"] + " - " + c["contacts"][0]["name"] + " (" + c["contacts"][0]["title"] + ")" for c in LUSHA_ROLES if c.get("contacts")]

    won_by_industry = {}
    won_by_country = {}
    for c in COMPANIES_WON:
        won_by_industry[c["industry"]] = won_by_industry.get(c["industry"], 0) + 1
        won_by_country[c["country"]] = won_by_country.get(c["country"], 0) + 1

    return f"""DATOS DISPONIBLES:

RECYCLING ({len(recycling_names)} empresas en pipeline BDR → Recycling):
{chr(10).join(recycling_names)}

INACTIVAS +45 DÍAS ({len(inactive_names)} empresas):
{chr(10).join(inactive_names)}

CLIENTES WON ({len(won_names)} empresas):
{chr(10).join(won_names)}
Por industria: {json.dumps(won_by_industry, ensure_ascii=False)}
Por país: {json.dumps(won_by_country, ensure_ascii=False)}

LUSHA NUEVAS ({len(lusha_names)} empresas NO en HubSpot):
{chr(10).join(lusha_names)}

LUSHA NUEVOS ROLES C-LEVEL RRHH ({len(lusha_roles_names)}):
{chr(10).join(lusha_roles_names)}

PRODUCTO HUMAND:
{chr(10).join(f"- {k}: {v}" for k,v in HUMAND_PRODUCT.items())}"""

@app.route("/api/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"answer": "Preguntame lo que necesites sobre empresas, clientes, o el producto de Humand.", "data": []})

    if not HAS_AI:
        return _fallback_search(q.lower())

    try:
        data_context = _build_data_context()
        response = ai_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=f"""Sos el buscador inteligente de BDRs Intelligence de Humand. Respondés preguntas sobre empresas, clientes, producto y prospección.

Tenés acceso a estos datos:
{data_context}

REGLAS:
- Respondé en español, directo y conciso (máximo 3-4 líneas).
- Si preguntan por empresas específicas, mencioná nombre, país, industria y empleados.
- Si preguntan cuántos clientes hay por industria/país, da los números exactos.
- Si preguntan sobre el producto de Humand, respondé con los datos que tenés.
- Si preguntan por empresas para prospectar, sugerí las de Lusha nuevas o Recycling según contexto.
- Si no tenés el dato, decilo honestamente.

Además de responder, devolvé un JSON con la acción para mostrar data en la tabla.
Tu respuesta debe ser SOLO un JSON válido con este formato:
{{"answer": "tu respuesta en texto", "type": "recycling|inactive|won|lusha_new|lusha_roles|none", "filters": {{"country": ""|"País", "industry": ""|"Industria", "min_employees": 0}}}}

type=none si la respuesta es solo texto sin tabla.""",
            messages=[{"role": "user", "content": q}]
        )

        text = response.content[0].text.strip()

        # Parse JSON response
        try:
            result = json.loads(text)
        except json.JSONDecodeError:
            # Try to extract JSON from response
            import re
            m = re.search(r'\{[\s\S]*\}', text)
            if m:
                result = json.loads(m.group())
            else:
                return jsonify({"answer": text, "data": []})

        answer = result.get("answer", text)
        data_type = result.get("type", "none")
        filters = result.get("filters", {})

        if data_type == "none":
            return jsonify({"answer": answer, "data": []})

        # Get the right data
        source_map = {
            "recycling": [c for c in COMPANIES_RECYCLING if not c.get("has_newer_cj_deal")],
            "inactive": COMPANIES_INACTIVE,
            "won": COMPANIES_WON,
            "lusha_new": LUSHA_NEW,
            "lusha_roles": LUSHA_ROLES,
        }
        data = source_map.get(data_type, [])

        # Apply AI-suggested filters
        f_country = filters.get("country", "")
        f_industry = filters.get("industry", "")
        f_min_emp = filters.get("min_employees", 0)

        if f_country:
            data = [c for c in data if c.get("country","").lower() == f_country.lower()]
        if f_industry:
            data = [c for c in data if c.get("industry","").lower() == f_industry.lower()]
        if f_min_emp:
            data = [c for c in data if c.get("employees",0) >= f_min_emp]

        return jsonify({"answer": answer, "data": data, "type": data_type})

    except Exception as e:
        print(f"[AI Search Error] {e}")
        return _fallback_search(q.lower())

def _fallback_search(q):
    """Keyword-based fallback when AI is not available."""
    for key, info in HUMAND_PRODUCT.items():
        if key in q:
            return jsonify({"answer": info, "data": []})

    if "cliente" in q or "won" in q or "ganado" in q or "cuantos" in q:
        results = COMPANIES_WON
        for c in ["méxico","colombia","argentina","perú","brasil"]:
            if c in q: results = [x for x in results if x["country"].lower() == c]
        for ind in ["retail","tecnología","salud","banca","manufactura"]:
            if ind in q: results = [x for x in results if x["industry"].lower() == ind]
        return jsonify({"answer": f"Tenemos {len(results)} clientes.", "data": results, "type": "won"})

    if "nueva" in q or "lusha" in q or "virgen" in q:
        import re
        emp_min = 0
        m = re.search(r'(\d+)', q)
        if m and int(m.group(1)) > 10: emp_min = int(m.group(1))
        results = [c for c in LUSHA_NEW if c["employees"] >= emp_min]
        return jsonify({"answer": f"Encontré {len(results)} empresas nuevas en Lusha.", "data": results, "type": "lusha_new"})

    if "recycling" in q or "retomar" in q:
        valid = [c for c in COMPANIES_RECYCLING if not c.get("has_newer_cj_deal")]
        return jsonify({"answer": f"Hay {len(valid)} empresas en Recycling.", "data": valid, "type": "recycling"})

    if "inactiv" in q or "45" in q:
        return jsonify({"answer": f"Hay {len(COMPANIES_INACTIVE)} empresas con +45 días sin actividad.", "data": COMPANIES_INACTIVE, "type": "inactive"})

    return jsonify({"answer": "No encontré algo específico. Probá preguntar: '¿cuántos clientes tenemos en Retail?', 'empresas nuevas con más de 500 empleados', '¿qué módulos tiene Humand?'", "data": []})

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
