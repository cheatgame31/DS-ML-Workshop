import streamlit as st

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="DS & ML Bootcamp",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------
SECTIONS = [
    {
        "label": "Day 1 · Python Foundations",
        "subtitle": "พื้นฐาน Python และการคิดแบบ Data",
        "icon": "🐍",
        "accent": "#7C3AED",
        "apps": [
            ("💰", "คำนวณส่วนลด", "คำนวณส่วนลดตามยอดซื้อของลูกค้า", "Beginner", "pages/app1_discount_calc.py"),
            ("📦", "วิเคราะห์คลังสินค้า", "สรุปมูลค่าสต๊อกและสินค้าที่ต้องสั่งซื้อ", "Inventory", "pages/energy_inventory.py"),
        ],
    },
    {
        "label": "Data Cleaning",
        "subtitle": "จัดการ Missing Value, Duplicate และข้อมูลผิดรูปแบบ",
        "icon": "🧼",
        "accent": "#06B6D4",
        "apps": [
            ("📂", "Customer Data Cleaner", "ทำความสะอาดข้อมูลลูกค้า", "Cleaning", "pages/clean_customers.py"),
            ("🐂", "Cleaning Workshop", "เวิร์กชอปทำความสะอาดข้อมูล", "Workshop", "pages/clean_app.py"),
            ("🥤", "Energy Drink Cleaning", "เคลียร์ข้อมูลยอดขายเครื่องดื่ม", "Sales Data", "pages/clean_energy_drink_sales.py"),
            ("🧽", "My Clean Data App", "เครื่องมือทำความสะอาดข้อมูลทั่วไป", "Utility", "pages/test.py"),
        ],
    },
    {
        "label": "Transform & EDA",
        "subtitle": "แปลงข้อมูล วิเคราะห์ และหา Insight จากข้อมูล",
        "icon": "📊",
        "accent": "#F59E0B",
        "apps": [
            ("🛠️", "Data Transformation", "แปลงและปรับรูปแบบข้อมูล", "Transform", "pages/transform_app.py"),
            ("💡", "EDA · Red Bull Sales", "สำรวจและวิเคราะห์ข้อมูลเชิงลึก", "Insight", "pages/EDA_app.py"),
        ],
    },
    {
        "label": "Machine Learning",
        "subtitle": "สร้างโมเดลทำนาย จำแนก และวิเคราะห์เชิงคาดการณ์",
        "icon": "🤖",
        "accent": "#10B981",
        "apps": [
            ("🎯", "High Sales Predictor", "จำแนกสินค้าขายดีด้วยโมเดล ML", "Classification", "pages/classify_redbull_sale.py"),
            ("📈", "Sales Prediction", "พยากรณ์ยอดขายล่วงหน้า", "Forecast", "pages/sale_predict.py"),
            ("🚛", "Logistics Prediction", "ทำนายเวลาบริการและจัดตารางขนส่ง", "Prediction", "pages/truck_predict.py"),
        ],
    },
]

# ----------------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Sarabun:wght@400;500;600;700;800&display=swap');

        :root {
            --bg-main: #F8FAFC;
            --card-bg: rgba(255,255,255,0.92);
            --text-main: #0F172A;
            --text-muted: #64748B;
            --border: rgba(148,163,184,0.22);
            --primary: #7C3AED;
            --primary-dark: #4C1D95;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', 'Sarabun', sans-serif;
        }

        body {
            background:
                radial-gradient(circle at top left, rgba(124,58,237,0.12), transparent 32%),
                radial-gradient(circle at top right, rgba(14,165,233,0.12), transparent 28%),
                linear-gradient(180deg, #F8FAFC 0%, #EEF2FF 100%);
        }

        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1240px;
        }

        /* ---------------- Hero ---------------- */
        .hero {
            position: relative;
            overflow: hidden;
            padding: 3.2rem 3rem;
            border-radius: 34px;
            color: #fff;
            background:
                radial-gradient(700px 300px at 20% 0%, rgba(129,140,248,0.55), transparent),
                radial-gradient(700px 300px at 100% 10%, rgba(34,211,238,0.35), transparent),
                linear-gradient(135deg, #111827 0%, #312E81 45%, #4C1D95 100%);
            box-shadow:
                0 30px 80px rgba(49,46,129,0.35),
                inset 0 1px 0 rgba(255,255,255,0.18);
            margin-bottom: 1.4rem;
        }

        .hero::before {
            content: "";
            position: absolute;
            width: 420px;
            height: 420px;
            right: -120px;
            top: -140px;
            background: rgba(255,255,255,0.08);
            border-radius: 999px;
            filter: blur(2px);
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.4fr 0.8fr;
            gap: 2rem;
            align-items: center;
            position: relative;
            z-index: 1;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.2);
            padding: 0.42rem 0.95rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 1.1rem;
            backdrop-filter: blur(10px);
        }

        .hero h1 {
            font-size: clamp(2.2rem, 5vw, 4.1rem);
            line-height: 1.02;
            margin: 0;
            font-weight: 900;
            letter-spacing: -0.055em;
        }

        .hero p {
            font-size: 1.08rem;
            line-height: 1.7;
            margin-top: 1rem;
            opacity: 0.86;
            max-width: 680px;
        }

        .hero-actions {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            margin-top: 1.5rem;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.72rem 1rem;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 999px;
            font-size: 0.9rem;
            font-weight: 700;
            backdrop-filter: blur(12px);
        }

        .stats-card {
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 28px;
            padding: 1.35rem;
            backdrop-filter: blur(18px);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.12);
        }

        .stats-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.9rem;
        }

        .stat {
            background: rgba(255,255,255,0.12);
            border-radius: 20px;
            padding: 1rem;
        }

        .stat .num {
            font-size: 1.8rem;
            font-weight: 900;
            letter-spacing: -0.04em;
        }

        .stat .label {
            font-size: 0.78rem;
            opacity: 0.75;
            margin-top: 0.1rem;
        }

        /* ---------------- Top summary ---------------- */
        .summary-wrap {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin: 1.4rem 0 1.5rem 0;
        }

        .summary-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 1.1rem 1.15rem;
            box-shadow: 0 8px 28px rgba(15,23,42,0.05);
        }

        .summary-card .k {
            color: var(--text-muted);
            font-size: 0.8rem;
            font-weight: 700;
        }

        .summary-card .v {
            color: var(--text-main);
            font-size: 1.45rem;
            font-weight: 900;
            margin-top: 0.25rem;
            letter-spacing: -0.04em;
        }

        /* ---------------- Streamlit widgets ---------------- */
        div[data-testid="stTextInput"] input {
            border-radius: 18px;
            border: 1px solid rgba(124,58,237,0.18);
            padding: 0.95rem 1rem;
            box-shadow: 0 8px 24px rgba(15,23,42,0.05);
        }

        div[data-testid="stTextInput"] label {
            font-weight: 800;
            color: #334155;
        }

        /* ---------------- Section ---------------- */
        .section-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin: 2.4rem 0 1rem 0;
        }

        .section-title-wrap {
            display: flex;
            align-items: center;
            gap: 0.9rem;
        }

        .section-icon {
            width: 46px;
            height: 46px;
            display: grid;
            place-items: center;
            border-radius: 16px;
            background: #fff;
            box-shadow: 0 8px 22px rgba(15,23,42,0.06);
            border: 1px solid var(--border);
            font-size: 1.25rem;
        }

        .section-title {
            font-size: 1.28rem;
            font-weight: 900;
            color: #0F172A;
            letter-spacing: -0.035em;
            margin: 0;
        }

        .section-subtitle {
            font-size: 0.9rem;
            color: #64748B;
            margin-top: 0.15rem;
        }

        .section-count {
            font-size: 0.78rem;
            font-weight: 800;
            color: #475569;
            background: #fff;
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 0.45rem 0.8rem;
        }

        /* ---------------- App buttons as cards ---------------- */
        div.stButton > button {
            width: 100%;
            min-height: 168px;
            padding: 0;
            border: none;
            background: transparent;
            box-shadow: none;
        }

        div.stButton > button:hover {
            background: transparent;
            border: none;
        }

        div.stButton > button p {
            margin: 0;
        }

        .app-card {
            height: 168px;
            text-align: left;
            border-radius: 26px;
            padding: 1.25rem;
            background:
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,255,255,0.90));
            border: 1px solid rgba(148,163,184,0.22);
            box-shadow:
                0 10px 28px rgba(15,23,42,0.06),
                inset 0 1px 0 rgba(255,255,255,0.75);
            transition: all .2s ease;
            position: relative;
            overflow: hidden;
        }

        .app-card::before {
            content: "";
            position: absolute;
            inset: 0;
            background: radial-gradient(380px 120px at 0% 0%, rgba(124,58,237,0.12), transparent);
            opacity: 0;
            transition: opacity .2s ease;
        }

        .app-card:hover {
            transform: translateY(-6px);
            border-color: rgba(124,58,237,0.42);
            box-shadow:
                0 20px 46px rgba(124,58,237,0.17),
                inset 0 1px 0 rgba(255,255,255,0.75);
        }

        .app-card:hover::before {
            opacity: 1;
        }

        .app-top {
            position: relative;
            z-index: 1;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 0.8rem;
        }

        .app-emoji {
            width: 48px;
            height: 48px;
            display: grid;
            place-items: center;
            border-radius: 17px;
            background: #F1F5F9;
            font-size: 1.45rem;
        }

        .badge {
            font-size: 0.72rem;
            font-weight: 800;
            color: #4C1D95;
            background: #F3E8FF;
            border: 1px solid rgba(124,58,237,0.18);
            padding: 0.3rem 0.62rem;
            border-radius: 999px;
        }

        .app-title {
            position: relative;
            z-index: 1;
            font-size: 1.06rem;
            font-weight: 900;
            color: #0F172A;
            margin-top: 1rem;
            letter-spacing: -0.025em;
        }

        .app-desc {
            position: relative;
            z-index: 1;
            color: #64748B;
            font-size: 0.87rem;
            line-height: 1.5;
            margin-top: 0.35rem;
        }

        .app-open {
            position: absolute;
            z-index: 1;
            right: 1.2rem;
            bottom: 1rem;
            color: #7C3AED;
            font-weight: 900;
            font-size: 0.9rem;
        }

        .empty-state {
            background: #fff;
            border: 1px dashed rgba(124,58,237,0.35);
            border-radius: 24px;
            padding: 2rem;
            text-align: center;
            color: #64748B;
            margin-top: 1.5rem;
        }

        .footer {
            margin-top: 3rem;
            padding: 1.2rem;
            text-align: center;
            color: #64748B;
            font-size: 0.85rem;
        }

        @media (max-width: 900px) {
            .hero-grid {
                grid-template-columns: 1fr;
            }

            .summary-wrap {
                grid-template-columns: repeat(2, 1fr);
            }

            .hero {
                padding: 2.3rem 1.5rem;
            }
        }

        @media (max-width: 600px) {
            .summary-wrap {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Helper
# ----------------------------------------------------------------------------
def app_card(emoji, title, desc, badge):
    return f"""
    <div class="app-card">
        <div class="app-top">
            <div class="app-emoji">{emoji}</div>
            <div class="badge">{badge}</div>
        </div>
        <div class="app-title">{title}</div>
        <div class="app-desc">{desc}</div>
        <div class="app-open">Open →</div>
    </div>
    """


# ----------------------------------------------------------------------------
# Hero
# ----------------------------------------------------------------------------
total_apps = sum(len(section["apps"]) for section in SECTIONS)
total_sections = len(SECTIONS)

st.markdown(
    f"""
    <div class="hero">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">🚀 7-Day Intensive Workshop</div>
                <h1>Data Science &<br/>Machine Learning<br/>Bootcamp</h1>
                <p>
                    ศูนย์รวมแอปพลิเคชันจากเวิร์กชอป สำหรับฝึก Python, Data Cleaning,
                    EDA และ Machine Learning พร้อมใช้งานในที่เดียว
                </p>
                <div class="hero-actions">
                    <div class="pill">⚡ Fast Access</div>
                    <div class="pill">📊 Data Apps</div>
                    <div class="pill">🤖 ML Ready</div>
                </div>
            </div>
            <div class="stats-card">
                <div class="stats-row">
                    <div class="stat">
                        <div class="num">{total_apps}</div>
                        <div class="label">Applications</div>
                    </div>
                    <div class="stat">
                        <div class="num">{total_sections}</div>
                        <div class="label">Learning Tracks</div>
                    </div>
                    <div class="stat">
                        <div class="num">7</div>
                        <div class="label">Workshop Days</div>
                    </div>
                    <div class="stat">
                        <div class="num">ML</div>
                        <div class="label">Final Track</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="summary-wrap">
        <div class="summary-card">
            <div class="k">Total Apps</div>
            <div class="v">{total_apps}</div>
        </div>
        <div class="summary-card">
            <div class="k">Learning Sections</div>
            <div class="v">{total_sections}</div>
        </div>
        <div class="summary-card">
            <div class="k">Focus Area</div>
            <div class="v">Data</div>
        </div>
        <div class="summary-card">
            <div class="k">Level</div>
            <div class="v">Bootcamp</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Search
# ----------------------------------------------------------------------------
search = st.text_input(
    "ค้นหาแอปที่ต้องการ",
    placeholder="เช่น cleaning, sales, prediction, EDA, logistics...",
)

query = search.strip().lower()

# ----------------------------------------------------------------------------
# App sections
# ----------------------------------------------------------------------------
found = 0
COLS_PER_ROW = 3

for section in SECTIONS:
    filtered_apps = []

    for app in section["apps"]:
        emoji, title, desc, badge, page = app
        text = f"{title} {desc} {badge} {section['label']}".lower()

        if query == "" or query in text:
            filtered_apps.append(app)

    if not filtered_apps:
        continue

    found += len(filtered_apps)

    st.markdown(
        f"""
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">{section["icon"]}</div>
                <div>
                    <div class="section-title">{section["label"]}</div>
                    <div class="section-subtitle">{section["subtitle"]}</div>
                </div>
            </div>
            <div class="section-count">{len(filtered_apps)} apps</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for i in range(0, len(filtered_apps), COLS_PER_ROW):
        row = filtered_apps[i : i + COLS_PER_ROW]
        cols = st.columns(COLS_PER_ROW, gap="large")

        for col, (emoji, title, desc, badge, page) in zip(cols, row):
            with col:
                clicked = st.button(
                    app_card(emoji, title, desc, badge),
                    key=page,
                    use_container_width=True,
                )
                if clicked:
                    st.switch_page(page)

# ----------------------------------------------------------------------------
# Empty state
# ----------------------------------------------------------------------------
if found == 0:
    st.markdown(
        """
        <div class="empty-state">
            <h3>ไม่พบแอปที่ค้นหา</h3>
            <p>ลองค้นหาด้วยคำอื่น เช่น sales, cleaning, prediction หรือ EDA</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        Made with ❤️ by Ruthapoom · DS & ML Bootcamp
    </div>
    """,
    unsafe_allow_html=True,
)
