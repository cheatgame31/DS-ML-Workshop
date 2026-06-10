import streamlit as st

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="DS & ML Bootcamp",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# App data
# ----------------------------------------------------------------------------
SECTIONS = [
    {
        "eyebrow": "FOUNDATION",
        "title": "Day 1 · Python & Data Basics",
        "sub": "เริ่มจาก logic, calculation และการจัดการข้อมูลพื้นฐานด้วย Python",
        "apps": [
            ("Discount Calculator", "ระบบคำนวณส่วนลดตามยอดซื้อ", "pages/app1_discount_calc.py", "01"),
            ("Inventory Analytics", "ระบบวิเคราะห์คลังสินค้า", "pages/energy_inventory.py", "02"),
        ],
    },
    {
        "eyebrow": "DATA PREPARATION",
        "title": "Data Cleaning",
        "sub": "เปลี่ยนข้อมูลดิบให้พร้อมสำหรับการวิเคราะห์และสร้างโมเดล",
        "apps": [
            ("Customer Data Cleaner", "ตรวจสอบและจัดระเบียบข้อมูลลูกค้า", "pages/clean_customers.py", "03"),
            ("Cleaning Workshop", "ฝึกจัดการ missing, duplicate และ outlier", "pages/clean_app.py", "04"),
            ("Energy Drink Sales", "เตรียมข้อมูลยอดขายเครื่องดื่ม", "pages/clean_energy_drink_sales.py", "05"),
            ("Clean Data Lab", "พื้นที่ทดลอง clean data", "pages/test.py", "06"),
        ],
    },
    {
        "eyebrow": "ANALYTICS",
        "title": "Transform & Exploratory Data Analysis",
        "sub": "แปลงข้อมูล สร้างมุมมอง และหา insight ก่อนเข้าสู่การทำ ML",
        "apps": [
            ("Data Transformation", "จัดรูปแบบและสร้าง feature สำหรับวิเคราะห์", "pages/transform_app.py", "07"),
            ("Red Bull Sales EDA", "สำรวจ pattern และ insight จากยอดขาย", "pages/EDA_app.py", "08"),
        ],
    },
    {
        "eyebrow": "MACHINE LEARNING",
        "title": "Prediction & Classification",
        "sub": "ประยุกต์ ML เพื่อทำนายยอดขายและเวลาการให้บริการโลจิสติกส์",
        "apps": [
            ("High Sales Predictor", "จำแนกโอกาสยอดขายสูง", "pages/classify_redbull_sale.py", "09"),
            ("Sales Prediction", "พยากรณ์ยอดขายจากข้อมูลย้อนหลัง", "pages/sale_predict.py", "10"),
            ("Logistics Time Prediction", "ทำนายระยะเวลาการให้บริการขนส่ง", "pages/truck_predict.py", "11"),
        ],
    },
]

TOTAL_APPS = sum(len(section["apps"]) for section in SECTIONS)

# ----------------------------------------------------------------------------
# Custom styling — executive, clean, not AI-slop
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sarabun:wght@400;500;600;700&display=swap');

        :root {
            --bg: #f7f8fb;
            --panel: #ffffff;
            --ink: #111827;
            --muted: #667085;
            --line: #e6e8ef;
            --brand: #1f4ed8;
            --brand-soft: #eef4ff;
            --shadow: 0 14px 40px rgba(16, 24, 40, 0.08);
        }

        html, body, [class*="css"] {
            font-family: 'Inter', 'Sarabun', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(31, 78, 216, 0.08), transparent 32rem),
                linear-gradient(180deg, #f8fafc 0%, #ffffff 42%);
        }

        footer, #MainMenu, header {visibility: hidden;}
        .block-container {
            max-width: 1180px;
            padding-top: 2.25rem;
            padding-bottom: 3rem;
        }

        /* ---------- Top bar ---------- */
        .topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        .brand-lockup {
            display: flex;
            align-items: center;
            gap: .75rem;
            color: var(--ink);
            font-weight: 800;
            letter-spacing: -.02em;
        }
        .brand-mark {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: grid;
            place-items: center;
            color: white;
            background: #111827;
            font-weight: 800;
        }
        .pill {
            display: inline-flex;
            align-items: center;
            gap: .45rem;
            padding: .45rem .7rem;
            border: 1px solid var(--line);
            border-radius: 999px;
            color: var(--muted);
            background: rgba(255,255,255,.8);
            font-size: .82rem;
            font-weight: 600;
        }

        /* ---------- Hero ---------- */
        .hero {
            border: 1px solid var(--line);
            background: rgba(255, 255, 255, 0.84);
            backdrop-filter: blur(10px);
            border-radius: 28px;
            padding: 2.3rem 2.25rem;
            box-shadow: var(--shadow);
            margin-bottom: 1.3rem;
            position: relative;
            overflow: hidden;
        }
        .hero:after {
            content: "";
            position: absolute;
            right: -8rem;
            top: -8rem;
            width: 18rem;
            height: 18rem;
            border-radius: 999px;
            background: rgba(31, 78, 216, 0.10);
        }
        .hero-grid {
            display: grid;
            grid-template-columns: minmax(0, 1.6fr) minmax(260px, .8fr);
            gap: 2rem;
            position: relative;
            z-index: 1;
        }
        .kicker {
            color: var(--brand);
            font-size: .78rem;
            font-weight: 800;
            letter-spacing: .12em;
            text-transform: uppercase;
            margin-bottom: .7rem;
        }
        .hero h1 {
            margin: 0;
            color: var(--ink);
            font-size: clamp(2.1rem, 4vw, 4.15rem);
            line-height: .98;
            letter-spacing: -.055em;
            font-weight: 800;
        }
        .hero p {
            max-width: 660px;
            color: var(--muted);
            font-size: 1.04rem;
            line-height: 1.75;
            margin: 1.05rem 0 0;
        }
        .hero-panel {
            border: 1px solid var(--line);
            border-radius: 22px;
            background: #fbfcff;
            padding: 1.2rem;
        }
        .metric-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: .75rem;
            margin-top: .95rem;
        }
        .metric {
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: .9rem;
            background: white;
        }
        .metric b {
            display: block;
            color: var(--ink);
            font-size: 1.45rem;
            line-height: 1;
        }
        .metric span {
            color: var(--muted);
            font-size: .78rem;
            font-weight: 600;
        }

        /* ---------- Sections ---------- */
        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            gap: 1rem;
            margin: 1.75rem 0 .75rem;
        }
        .section-eyebrow {
            color: var(--brand);
            font-size: .72rem;
            font-weight: 800;
            letter-spacing: .12em;
            text-transform: uppercase;
            margin-bottom: .25rem;
        }
        .section-title {
            color: var(--ink);
            font-size: 1.32rem;
            font-weight: 800;
            letter-spacing: -.025em;
            margin: 0;
        }
        .section-sub {
            color: var(--muted);
            font-size: .92rem;
            margin-top: .2rem;
        }

        /* ---------- Streamlit buttons as cards ---------- */
        div.stButton > button {
            width: 100%;
            min-height: 132px;
            border-radius: 20px;
            border: 1px solid var(--line);
            background: rgba(255,255,255,0.94);
            color: var(--ink);
            box-shadow: 0 6px 18px rgba(16, 24, 40, 0.045);
            padding: 1.05rem 1rem;
            text-align: left;
            white-space: pre-line;
            line-height: 1.38;
            font-weight: 700;
            transition: all .16s ease;
        }
        div.stButton > button p {
            font-size: .98rem;
            line-height: 1.38;
        }
        div.stButton > button:hover {
            border-color: rgba(31, 78, 216, 0.38);
            background: #ffffff;
            transform: translateY(-2px);
            box-shadow: 0 16px 34px rgba(31, 78, 216, 0.12);
            color: var(--brand);
        }
        div.stButton > button:active {
            transform: translateY(0px);
        }

        .footer-note {
            margin-top: 2rem;
            padding: 1rem 1.1rem;
            border: 1px solid var(--line);
            border-radius: 18px;
            color: var(--muted);
            background: #fff;
            font-size: .88rem;
        }

        /* ---------- Sidebar ---------- */
        [data-testid="stSidebar"] {
            background: #0f172a;
        }
        [data-testid="stSidebar"] * {
            color: #e5e7eb;
        }
        [data-testid="stSidebar"] .stCaptionContainer,
        [data-testid="stSidebar"] p {
            color: #cbd5e1;
        }

        @media (max-width: 820px) {
            .hero-grid { grid-template-columns: 1fr; }
            .topbar { align-items: flex-start; flex-direction: column; }
            .hero { padding: 1.6rem; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="topbar">
        <div class="brand-lockup">
            <div class="brand-mark">DS</div>
            <div>Data Science & ML Bootcamp</div>
        </div>
        <div class="pill">7-Day Hands-on Workshop</div>
    </div>

    <div class="hero">
        <div class="hero-grid">
            <div>
                <div class="kicker">Learning Portal</div>
                <h1>Build practical data skills, one app at a time.</h1>
                <p>
                    รวมเครื่องมือฝึกปฏิบัติสำหรับ Python, Data Cleaning, EDA และ Machine Learning
                    ในหน้าเดียวที่ใช้งานง่าย ดูสะอาด และพร้อมใช้เป็น training portal สำหรับ workshop
                </p>
            </div>
            <div class="hero-panel">
                <div class="kicker">Bootcamp Snapshot</div>
                <div class="metric-row">
                    <div class="metric"><b>{len(SECTIONS)}</b><span>Learning Tracks</span></div>
                    <div class="metric"><b>{TOTAL_APPS}</b><span>Practice Apps</span></div>
                </div>
                <div class="metric-row">
                    <div class="metric"><b>ML</b><span>Prediction Focus</span></div>
                    <div class="metric"><b>EDA</b><span>Insight Driven</span></div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Render menu
# ----------------------------------------------------------------------------
COLS_PER_ROW = 3

for section in SECTIONS:
    st.markdown(
        f"""
        <div class="section-head">
            <div>
                <div class="section-eyebrow">{section['eyebrow']}</div>
                <h2 class="section-title">{section['title']}</h2>
                <div class="section-sub">{section['sub']}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    apps = section["apps"]
    for i in range(0, len(apps), COLS_PER_ROW):
        cols = st.columns(COLS_PER_ROW, gap="medium")
        for col, (title, desc, page, number) in zip(cols, apps[i : i + COLS_PER_ROW]):
            with col:
                button_text = f"{number}\n{title}\n{desc}"
                if st.button(button_text, key=page):
                    st.switch_page(page)

st.markdown(
    """
    <div class="footer-note">
        Designed for focused learning: minimal decoration, clear hierarchy, and app cards that help learners choose the next exercise quickly.
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## DS & ML Bootcamp")
    st.caption("Training portal for hands-on data applications")
    st.divider()

    st.markdown("**Workshop flow**")
    st.markdown("1. Python Basics")
    st.markdown("2. Data Cleaning")
    st.markdown("3. Transformation & EDA")
    st.markdown("4. Machine Learning")

    st.divider()
    st.caption("Created by Ruthapoom")
