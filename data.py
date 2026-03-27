# ── WON CLIENTS (20 empresas) ─────────────────────────────────────
COMPANIES_WON = [
    {"name": "Grupo Éxito", "country": "Colombia", "industry": "Retail", "employees": 42000, "since": "2023", "deal_stage": "Won"},
    {"name": "Banco Davivienda", "country": "Colombia", "industry": "Banca", "employees": 18000, "since": "2022", "deal_stage": "Won"},
    {"name": "OXXO", "country": "México", "industry": "Retail", "employees": 90000, "since": "2021", "deal_stage": "Won"},
    {"name": "Bimbo", "country": "México", "industry": "Alimentación", "employees": 130000, "since": "2021", "deal_stage": "Won"},
    {"name": "FEMSA", "country": "México", "industry": "Retail", "employees": 320000, "since": "2022", "deal_stage": "Won"},
    {"name": "Grupo Posadas", "country": "México", "industry": "Turismo", "employees": 15000, "since": "2023", "deal_stage": "Won"},
    {"name": "Swiss Medical", "country": "Argentina", "industry": "Salud", "employees": 12000, "since": "2022", "deal_stage": "Won"},
    {"name": "Arcelor Mittal", "country": "Argentina", "industry": "Manufactura", "employees": 8500, "since": "2021", "deal_stage": "Won"},
    {"name": "Tenaris", "country": "Argentina", "industry": "Manufactura", "employees": 22000, "since": "2020", "deal_stage": "Won"},
    {"name": "Siemens", "country": "España", "industry": "Tecnología", "employees": 45000, "since": "2023", "deal_stage": "Won"},
    {"name": "John Deere", "country": "USA", "industry": "Manufactura", "employees": 82000, "since": "2022", "deal_stage": "Won"},
    {"name": "The Home Depot", "country": "USA", "industry": "Retail", "employees": 475000, "since": "2023", "deal_stage": "Won"},
    {"name": "Nemak", "country": "México", "industry": "Automotriz", "employees": 24000, "since": "2022", "deal_stage": "Won"},
    {"name": "MINISO", "country": "México", "industry": "Retail", "employees": 8000, "since": "2023", "deal_stage": "Won"},
    {"name": "PSBank", "country": "Colombia", "industry": "Banca", "employees": 5500, "since": "2023", "deal_stage": "Won"},
    {"name": "MRV&CO", "country": "Brasil", "industry": "Construcción", "employees": 32000, "since": "2022", "deal_stage": "Won"},
    {"name": "Belcorp", "country": "Perú", "industry": "Cosméticos", "employees": 9200, "since": "2023", "deal_stage": "Won"},
    {"name": "EssilorLuxottica", "country": "Colombia", "industry": "Salud", "employees": 190000, "since": "2022", "deal_stage": "Won"},
    {"name": "Efecty", "country": "Colombia", "industry": "Finanzas", "employees": 6000, "since": "2023", "deal_stage": "Won"},
    {"name": "Intercorp", "country": "Perú", "industry": "Retail", "employees": 35000, "since": "2022", "deal_stage": "Won"},
]

# ── RECYCLING (sorted by most recent first) ──────────────────────
COMPANIES_RECYCLING = [
    {"name": "Farmacias Unidas", "country": "Colombia", "industry": "Farmacéutica", "employees": 4500, "deal_stage": "Recycling", "days_inactive": 47, "last_activity": "2026-02-08"},
    {"name": "Hotel Pacífico", "country": "México", "industry": "Turismo", "employees": 3500, "deal_stage": "Recycling", "days_inactive": 52, "last_activity": "2026-02-03"},
    {"name": "Seguros Continental", "country": "Colombia", "industry": "Seguros", "employees": 750, "deal_stage": "Recycling", "days_inactive": 58, "last_activity": "2026-01-28"},
    {"name": "Laboratorios Biomed", "country": "México", "industry": "Farmacéutica", "employees": 1100, "deal_stage": "Recycling", "days_inactive": 65, "last_activity": "2026-01-21"},
    {"name": "Grupo Alimenticio Dorado", "country": "México", "industry": "Alimentación", "employees": 3200, "deal_stage": "Recycling", "days_inactive": 72, "last_activity": "2026-01-14"},
    {"name": "Cementos del Valle", "country": "Colombia", "industry": "Construcción", "employees": 2800, "deal_stage": "Recycling", "days_inactive": 80, "last_activity": "2026-01-06"},
    {"name": "TechVentures", "country": "Argentina", "industry": "Tecnología", "employees": 80, "deal_stage": "Recycling", "days_inactive": 90, "last_activity": "2025-12-27"},
    {"name": "Energía Solar MX", "country": "México", "industry": "Energía", "employees": 95, "deal_stage": "Recycling", "days_inactive": 105, "last_activity": "2025-12-12"},
    {"name": "FinTech Nova", "country": "Argentina", "industry": "Fintech", "employees": 200, "deal_stage": "Recycling", "days_inactive": 120, "last_activity": "2025-11-27"},
    {"name": "Construcciones Vial", "country": "Colombia", "industry": "Construcción", "employees": 450, "deal_stage": "Recycling", "days_inactive": 135, "last_activity": "2025-11-12"},
]

# ── INACTIVE +45 DAYS ─────────────────────────────────────────────
COMPANIES_INACTIVE = [
    {"name": "AutoPartes Nacional", "country": "Argentina", "industry": "Automotriz", "employees": 1400, "deal_stage": "Engagement", "days_inactive": 67, "last_activity": "2026-01-20"},
    {"name": "Cadena Supermercados Plus", "country": "México", "industry": "Retail", "employees": 4000, "deal_stage": "Approaching", "days_inactive": 77, "last_activity": "2026-01-10"},
    {"name": "AgriTech Patagonia", "country": "Argentina", "industry": "Agricultura", "employees": 210, "deal_stage": "Approaching", "days_inactive": 64, "last_activity": "2026-01-22"},
    {"name": "Despegar", "country": "Argentina", "industry": "Turismo", "employees": 2800, "deal_stage": "Lead", "days_inactive": 76, "last_activity": "2026-01-10"},
    {"name": "Grupo Lala", "country": "México", "industry": "Alimentación", "employees": 18000, "deal_stage": "Contacted", "days_inactive": 81, "last_activity": "2026-01-05"},
    {"name": "Habi", "country": "Colombia", "industry": "PropTech", "employees": 760, "deal_stage": "Lead", "days_inactive": 64, "last_activity": "2026-01-22"},
    {"name": "CloudOps", "country": "Argentina", "industry": "Tecnología", "employees": 155, "deal_stage": "Approaching", "days_inactive": 50, "last_activity": "2026-02-05"},
    {"name": "Banco Central Corp", "country": "Argentina", "industry": "Finanzas", "employees": 850, "deal_stage": "Pre-Qualified", "days_inactive": 48, "last_activity": "2026-02-07"},
]

# ── LUSHA NEW (not in HubSpot) ────────────────────────────────────
LUSHA_NEW = [
    {"name": "Rappi", "country": "Colombia", "industry": "Tecnología", "employees": 3200, "contacts": [
        {"name": "Valentina Ospina", "title": "VP de Recursos Humanos", "email": "v.ospina@rappi.com", "linkedin": "https://linkedin.com/in/valentina-ospina-rappi", "lusha": "https://app.lusha.com/person/valentina-ospina"},
        {"name": "Andrés Gómez", "title": "Chief People Officer", "email": "a.gomez@rappi.com", "linkedin": "https://linkedin.com/in/andres-gomez-rappi", "lusha": "https://app.lusha.com/person/andres-gomez"}
    ], "linkedin_company": "https://linkedin.com/company/rappi"},
    {"name": "Nubank", "country": "Brasil", "industry": "Fintech", "employees": 8000, "contacts": [
        {"name": "Fernanda Almeida", "title": "Chief People Officer", "email": "f.almeida@nubank.com.br", "linkedin": "https://linkedin.com/in/fernanda-almeida-nu", "lusha": "https://app.lusha.com/person/fernanda-almeida"},
        {"name": "Rafael Costa", "title": "VP People", "email": "r.costa@nubank.com.br", "linkedin": "https://linkedin.com/in/rafael-costa-nu", "lusha": "https://app.lusha.com/person/rafael-costa"}
    ], "linkedin_company": "https://linkedin.com/company/nubank"},
    {"name": "Grupo Industrial Saltillo", "country": "México", "industry": "Manufactura", "employees": 4200, "contacts": [
        {"name": "Roberto Garza Medina", "title": "CHRO", "email": "rgarza@gis.com.mx", "linkedin": "https://linkedin.com/in/roberto-garza-medina", "lusha": "https://app.lusha.com/person/roberto-garza-medina"},
        {"name": "Mariana López Treviño", "title": "VP de Recursos Humanos", "email": "mlopez@gis.com.mx", "linkedin": "https://linkedin.com/in/mariana-lopez-trevino", "lusha": "https://app.lusha.com/person/mariana-lopez-trevino"}
    ], "linkedin_company": "https://linkedin.com/company/gis"},
    {"name": "Farmacias del Ahorro", "country": "México", "industry": "Retail", "employees": 18000, "contacts": [
        {"name": "Patricia Hernández Mora", "title": "Directora de Personas", "email": "phernandez@fahorro.com", "linkedin": "https://linkedin.com/in/patricia-hernandez-mora", "lusha": "https://app.lusha.com/person/patricia-hernandez-mora"}
    ], "linkedin_company": "https://linkedin.com/company/fahorro"},
    {"name": "Kushki", "country": "Ecuador", "industry": "Fintech", "employees": 520, "contacts": [
        {"name": "Isabella Andrade", "title": "People Director", "email": "i.andrade@kushkipagos.com", "linkedin": "https://linkedin.com/in/isabella-andrade-kushki", "lusha": "https://app.lusha.com/person/isabella-andrade"}
    ], "linkedin_company": "https://linkedin.com/company/kushki"},
    {"name": "Fintual", "country": "Uruguay", "industry": "Fintech", "employees": 380, "contacts": [
        {"name": "Ignacio Herrera", "title": "Head of HR", "email": "i.herrera@fintual.com", "linkedin": "https://linkedin.com/in/ignacio-herrera-fintual", "lusha": "https://app.lusha.com/person/ignacio-herrera"}
    ], "linkedin_company": "https://linkedin.com/company/fintual"},
    {"name": "PayRetailers", "country": "España", "industry": "Fintech", "employees": 310, "contacts": [
        {"name": "Elena Fuentes", "title": "Chief People Officer", "email": "e.fuentes@payretailers.com", "linkedin": "https://linkedin.com/in/elena-fuentes-payretailers", "lusha": "https://app.lusha.com/person/elena-fuentes"}
    ], "linkedin_company": "https://linkedin.com/company/payretailers"},
    {"name": "Kavak", "country": "México", "industry": "Automotriz", "employees": 4500, "contacts": [
        {"name": "Carlos Mendez Ruiz", "title": "CHRO", "email": "c.mendez@kavak.com", "linkedin": "https://linkedin.com/in/carlos-mendez-kavak", "lusha": "https://app.lusha.com/person/carlos-mendez-kavak"}
    ], "linkedin_company": "https://linkedin.com/company/kavak"},
]

# ── LUSHA ROLES (new C-level HR roles in existing accounts) ───────
LUSHA_ROLES = [
    {"name": "Globalink Solutions", "country": "Argentina", "industry": "Tecnología", "employees": 1200, "deal_stage": "Demo", "contacts": [
        {"name": "Valentina Cruz", "title": "Chief People Officer", "email": "v.cruz@globalink.com", "linkedin": "https://linkedin.com/in/valentina-cruz", "lusha": "https://app.lusha.com/person/valentina-cruz", "note": "Nueva CPO — anterior estuvo 6 años"}
    ], "linkedin_company": "https://linkedin.com/company/globalink"},
    {"name": "TechBridge SA", "country": "México", "industry": "Tecnología", "employees": 850, "deal_stage": "Discovery", "contacts": [
        {"name": "Rodrigo Sánchez", "title": "VP de Recursos Humanos", "email": "r.sanchez@techbridge.mx", "linkedin": "https://linkedin.com/in/rodrigo-sanchez", "lusha": "https://app.lusha.com/person/rodrigo-sanchez", "note": "Nuevo VP — viene de Cemex"}
    ], "linkedin_company": "https://linkedin.com/company/techbridge"},
    {"name": "Nexus Consulting", "country": "Colombia", "industry": "Consultoría", "employees": 620, "deal_stage": "Lead", "contacts": [
        {"name": "Camila Morales", "title": "CHRO", "email": "c.morales@nexusconsulting.co", "linkedin": "https://linkedin.com/in/camila-morales", "lusha": "https://app.lusha.com/person/camila-morales", "note": "Primera vez que tienen CHRO"}
    ], "linkedin_company": "https://linkedin.com/company/nexus-consulting"},
    {"name": "DataFlow Corp", "country": "Argentina", "industry": "Tecnología", "employees": 430, "deal_stage": "Demo", "contacts": [
        {"name": "Andrés Pereira", "title": "Director de People & Culture", "email": "a.pereira@dataflow.cl", "linkedin": "https://linkedin.com/in/andres-pereira", "lusha": "https://app.lusha.com/person/andres-pereira", "note": "Reemplazó al anterior que se fue"}
    ], "linkedin_company": "https://linkedin.com/company/dataflow"},
    {"name": "Orion Manufacturing", "country": "Argentina", "industry": "Manufactura", "employees": 3400, "deal_stage": "Discovery", "contacts": [
        {"name": "Luciana Ferrari", "title": "Head of HR", "email": "l.ferrari@orionmfg.com.ar", "linkedin": "https://linkedin.com/in/luciana-ferrari", "lusha": "https://app.lusha.com/person/luciana-ferrari", "note": "Nueva — cambio de estructura"}
    ], "linkedin_company": "https://linkedin.com/company/orion-manufacturing"},
    {"name": "Atlas Retail", "country": "Argentina", "industry": "Retail", "employees": 12000, "deal_stage": "Demo", "contacts": [
        {"name": "Nicolás Reyes", "title": "Chief Human Resources Officer", "email": "n.reyes@atlasretail.com.ar", "linkedin": "https://linkedin.com/in/nicolas-reyes", "lusha": "https://app.lusha.com/person/nicolas-reyes", "note": "Nuevo CHRO — viene del sector bancario"}
    ], "linkedin_company": "https://linkedin.com/company/atlas-retail"},
]

# ── HUMAND PRODUCT INFO ───────────────────────────────────────────
HUMAND_PRODUCT = {
    "humand": "Humand es una plataforma todo en uno que centraliza la gestión de RRHH, comunicación interna, onboarding y cultura empresarial en una sola app desde el celular. +1.500 empresas la usan, 1.6M usuarios activos, 4.9/5 en app stores. USD 66M levantados (Kaszek + Goodwater).",
    "módulo": "Humand tiene 30+ módulos: Chat, Red Social Interna, Live Streaming, Noticias, Organigrama, Biblioteca, Beneficios, Documentos, Onboarding, Expediente Digital, Asistencia, Reserva de Espacios, Políticas, Vacaciones, Evaluación de Desempeño, OKRs, LMS, Plan de Carrera, Búsquedas Internas, Encuestas, Reconocimientos, Eventos, Marketplace, Referidos, Cumpleaños, People Experience, Formularios, Gestión de Servicios, IA y Chatbots.",
    "comunicación": "Módulos de comunicación interna: Chat (texto, voz, video), Red Social Interna (grupos, publicaciones), Live Streaming (townhalls), Noticias (anuncios), Organigrama, Biblioteca de Recursos, Beneficios.",
    "onboarding": "Onboarding digital: el nuevo empleado recibe todo en la app — documentos para firmar, capacitaciones obligatorias, contactos clave, bienvenida del equipo. Empresas similares redujeron el tiempo de onboarding un 60%.",
    "evaluación": "Evaluación de desempeño configurable: 360°, 180°, por competencias, con feedback continuo y dashboards en tiempo real.",
    "vacaciones": "Gestión de vacaciones y permisos 100% digital: el empleado pide desde la app, el jefe aprueba con un click, se descuenta automáticamente del saldo.",
    "integra": "Humand se integra con SAP, sistemas de nómina, SSO (Azure AD, SAML), webhooks y tiene API abierta.",
    "segur": "Plataforma enterprise con encriptación, permisos por rol, SSO, cumplimiento de normativas de protección de datos.",
    "precio": "El pricing depende del número de empleados y módulos. ROI promedio en 6 meses. Ahorro de ~5 horas por empleado por semana.",
    "lms": "LMS mobile: subís cursos y el empleado los completa desde su celular. Quizzes, certificaciones, y registro para auditorías.",
    "reconocimiento": "Módulo de Reconocimientos (Kudos): líderes y compañeros dan reconocimientos. Mejora engagement y retención.",
    "encuesta": "Encuestas de clima con analytics en tiempo real. Podés medir eNPS por planta, turno o área. Resultados instantáneos.",
    "formulario": "Formularios y aprobaciones digitales: creás el flujo una vez, se enruta automáticamente. Notificación push, firma digital, trazabilidad.",
}
