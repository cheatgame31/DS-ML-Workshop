import streamlit as st

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="DS & ML Bootcamp",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# Custom styling: cleaner Nintendo-inspired learning hub
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Sarabun:wght@400;500;600;700;800&display=swap');

        :root {
            --red: #e60012;
            --red-dark: #b0000d;
            --ink: #18181b;
            --sub: #5f6470;
            --line: #e8e8ec;
            --soft: #f6f6f8;
            --card: #ffffff;
            --shadow: 0 10px 28px rgba(17, 24, 39, 0.07);
            --radius-xl: 28px;
            --radius-lg: 22px;
            --radius-md: 18px;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', 'Sarabun', sans-serif;
            color: var(--ink);
        }

        .stApp {
            background:
                radial-gradient(circle at 0% 0%, rgba(230,0,18,0.06), transparent 24%),
                radial-gradient(circle at 100% 0%, rgba(230,0,18,0.04), transparent 18%),
                linear-gradient(180deg, #ffffff 0%, #fafafb 100%);
        }

        header, footer, #MainMenu {visibility: hidden;}
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}

        .block-container {
            max-width: 1240px;
            padding-top: 1.15rem;
            padding-bottom: 4rem;
        }

        /* top nav */
        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 1rem;
            background: rgba(255,255,255,0.88);
            backdrop-filter: blur(10px);
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: 0.7rem 0.85rem;
            box-shadow: 0 8px 24px rgba(17, 24, 39, 0.05);
        }
        .brand-wrap {
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        .brand-badge {
            background: var(--red);
            color: white;
            border-radius: 999px;
            padding: 0.45rem 0.95rem;
            font-size: 0.9rem;
            font-weight: 900;
            letter-spacing: -0.02em;
        }
        .brand-copy { line-height: 1.1; }
        .brand-title {
            font-size: 0.98rem;
            font-weight: 900;
            letter-spacing: -0.03em;
        }
        .brand-sub {
            font-size: 0.78rem;
            color: var(--sub);
            font-weight: 600;
        }
        .nav-links {
            display: flex;
            gap: 0.45rem;
            flex-wrap: wrap;
            justify-content: flex-end;
        }
        .nav-link {
            border: 1px solid var(--line);
            background: white;
            color: #323742;
            border-radius: 999px;
            padding: 0.42rem 0.78rem;
            font-size: 0.8rem;
            font-weight: 800;
        }

        /* hero */
        .hero {
            position: relative;
            overflow: hidden;
            border-radius: 34px;
            background: linear-gradient(135deg, #ef0015 0%, #d90012 58%, #b40011 100%);
            color: white;
            padding: 2.4rem 2.2rem;
            box-shadow: 0 20px 44px rgba(230,0,18,0.22);
            margin-bottom: 1.15rem;
        }
        .hero:before {
            content: "";
            position: absolute;
            width: 420px;
            height: 420px;
            border-radius: 50%;
            background: rgba(255,255,255,0.09);
            right: -100px;
            bottom: -180px;
        }
        .hero:after {
            content: "";
            position: absolute;
            width: 190px;
            height: 190px;
            border-radius: 50%;
            border: 28px solid rgba(255,255,255,0.10);
            right: 110px;
            top: -55px;
        }
        .hero-inner {
            position: relative;
            z-index: 2;
            max-width: 760px;
        }
        .hero-kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.25);
            padding: 0.45rem 0.8rem;
            font-size: 0.82rem;
            font-weight: 800;
            margin-bottom: 0.95rem;
        }
        .hero h1 {
            margin: 0;
            font-size: clamp(2.3rem, 5vw, 4.3rem);
            line-height: 0.96;
            letter-spacing: -0.06em;
            font-weight: 900;
        }
        .hero p {
            margin: 1rem 0 0 0;
            max-width: 650px;
            font-size: 1.02rem;
            line-height: 1.7;
            font-weight: 500;
            opacity: 0.96;
        }
        .hero-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
            margin-top: 1.2rem;
        }
        .hero-tag {
            background: white;
            color: var(--red);
            border-radius: 999px;
            padding: 0.54rem 0.9rem;
            font-size: 0.84rem;
            font-weight: 900;
        }
        .hero-tag.alt {
            background: rgba(0,0,0,0.18);
            color: white;
            border: 1px solid rgba(255,255,255,0.24);
        }

        /* metrics */
        .metrics {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.9rem;
            margin: 1rem 0 1.55rem 0;
        }
        .metric {
            background: rgba(255,255,255,0.95);
            border: 1px solid var(--line);
            border-radius: 22px;
            padding: 1rem 1.05rem;
            box-shadow: var(--shadow);
        }
        .metric-no {
            font-size: 1.75rem;
            line-height: 1;
            font-weight: 900;
            letter-spacing: -0.05em;
            color: var(--red);
        }
        .metric-label {
            margin-top: 0.35rem;
            font-size: 0.85rem;
            color: var(--sub);
            font-weight: 700;
        }

        /* section */
        .section-wrap { margin-top: 1.8rem; }
        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            gap: 1rem;
            margin-bottom: 0.85rem;
        }
        .section-left {
            display: flex;
            align-items: center;
            gap: 0.9rem;
        }
        .section-no {
            min-width: 48px;
            height: 48px;
            border-radius: 16px;
            display: grid;
            place-items: center;
            background: var(--red);
            color: white;
            font-size: 1rem;
            font-weight: 900;
            box-shadow: 0 12px 26px rgba(230,0,18,0.18);
        }
        .section-title {
            margin: 0;
            font-size: 1.95rem;
            line-height: 1.0;
            font-weight: 900;
            letter-spacing: -0.05em;
        }
        .section-sub {
            margin: 0.35rem 0 0 0;
            font-size: 0.95rem;
            line-height: 1.55;
            color: var(--sub);
            font-weight: 600;
        }
        .section-pill {
            background: white;
            border: 1px solid var(--line);
            color: var(--sub);
            border-radius: 999px;
            padding: 0.38rem 0.7rem;
            font-size: 0.8rem;
            font-weight: 800;
        }

        /* app cards */
        .app-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 24px;
            padding: 1rem 1rem 0.7rem 1rem;
            box-shadow: var(--shadow);
            min-height: 176px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            margin-bottom: 0.55rem;
        }
        .app-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 0.65rem;
            margin-bottom: 0.7rem;
        }
        .app-code {
            background: #fff4f5;
            color: var(--red);
            border: 1px solid #ffdadd;
            border-radius: 999px;
            padding: 0.22rem 0.58rem;
            font-size: 0.72rem;
            font-weight: 900;
            letter-spacing: 0.04em;
        }
        .app-type {
            font-size: 0.74rem;
            color: var(--sub);
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }
        .app-title {
            font-size: 1.08rem;
            line-height: 1.2;
            font-weight: 900;
            letter-spacing: -0.03em;
            margin: 0 0 0.35rem 0;
            color: var(--ink);
        }
        .app-desc {
            margin: 0;
            font-size: 0.88rem;
            line-height: 1.55;
            color: var(--sub);
            font-weight: 500;
        }

        div.stButton > button {
            width: 100%;
            min-height: 44px;
            border-radius: 999px;
            border: 1px solid var(--red);
            background: var(--red);
            color: white;
            font-size: 0.92rem;
            font-weight: 800;
            box-shadow: 0 8px 18px rgba(230,0,18,0.16);
            transition: all 0.15s ease;
        }
        div.stButton > button:hover {
            background: var(--red-dark);
            border-color: var(--red-dark);
            transform: translateY(-1px);
        }
        div.stButton > button:active {
            transform: translateY(0);
        }

        /* sidebar */
        [data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid var(--line);
        }
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: var(--red);
            letter-spacing: -0.03em;
            font-weight: 900;
        }
        .side-panel {
            background: white;
            border: 1px solid var(--line);
            border-radius: 22px;
            padding: 1rem;
            margin: 0.75rem 0;
            box-shadow: 0 8px 22px rgba(17,24,39,0.04);
        }
        .side-badge {
            display: inline-block;
            background: var(--red);
            color: white;
            border-radius: 999px;
            padding: 0.26rem 0.56rem;
            font-size: 0.72rem;
            font-weight: 900;
            margin-bottom: 0.55rem;
        }
        .side-heading {
            font-size: 1rem;
            font-weight: 900;
            margin-bottom: 0.35rem;
            color: var(--ink);
        }
        .side-copy {
            color: var(--sub);
            font-size: 0.86rem;
            line-height: 1.55;
        }

        @media (max-width: 1000px) {
            .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .topbar { flex-direction: column; align-items: flex-start; border-radius: 28px; }
            .section-head { flex-direction: column; align-items: flex-start; }
            .section-title { font-size: 1.65rem; }
        }
        @media (max-width: 640px) {
            .metrics { grid-template-columns: 1fr; }
            .hero { padding: 1.8rem 1.25rem; border-radius: 28px; }
            .hero h1 { font-size: 2.2rem; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Data structure
# ----------------------------------------------------------------------------
SECTIONS = [
    {
        "code": "01",
        "title": "Day 1 · Python & Data Basics",
        "sub": "พื้นฐานการคำนวณ โครงสร้างข้อมูล และโจทย์ธุรกิจเบื้องต้น",
        "apps": [
            {
                "tag": "DAY 1",
                "title": "Discount Calculator",
                "desc": "ระบบคำนวณส่วนลดตามยอดซื้อ เพื่อฝึกเงื่อนไขและการคำนวณด้วย Python",
                "page": "pages/app1_discount_calc.py",
            },
            {
                "tag": "DAY 1",
                "title": "Inventory Analytics",
                "desc": "ระบบวิเคราะห์คลังสินค้าเบื้องต้น เพื่อฝึกการอ่านข้อมูลและสรุปผล",
                "page": "pages/energy_inventory.py",
            },
        ],
    },
    {
        "code": "02",
        "title": "Data Cleaning",
        "sub": "จัดการ Missing, Duplicate และรูปแบบข้อมูลให้พร้อมสำหรับงานวิเคราะห์",
        "apps": [
            {
                "tag": "CLEAN",
                "title": "Customer Data Cleaner",
                "desc": "เตรียมข้อมูลลูกค้าให้สะอาด พร้อมใช้งานสำหรับการวิเคราะห์และสร้างโมเดล",
                "page": "pages/clean_customers.py",
            },
            {
                "tag": "WORKSHOP",
                "title": "Data Cleaning Workshop",
                "desc": "แบบฝึกหัดทำความสะอาดข้อมูลแบบ interactive สำหรับผู้เริ่มต้น",
                "page": "pages/clean_app.py",
            },
            {
                "tag": "SALES",
                "title": "Energy Drink Sales Cleaning",
                "desc": "ทำความสะอาดข้อมูลยอดขายเพื่อเตรียมใช้ต่อในงาน EDA และ Machine Learning",
                "page": "pages/clean_energy_drink_sales.py",
            },
            {
                "tag": "PRACTICE",
                "title": "My App Clean Data",
                "desc": "ทดลองล้างข้อมูลด้วย workflow แบบง่าย เหมาะสำหรับการฝึกซ้ำ",
                "page": "pages/test.py",
            },
        ],
    },
    {
        "code": "03",
        "title": "Transform & EDA",
        "sub": "แปลงข้อมูล สร้างกราฟ และค้นหา pattern เพื่อสร้าง insight ให้ธุรกิจ",
        "apps": [
            {
                "tag": "TRANSFORM",
                "title": "Data Transformation App",
                "desc": "แปลงข้อมูลเพื่อให้พร้อมสำหรับการวิเคราะห์และต่อยอดใน pipeline ถัดไป",
                "page": "pages/transform_app.py",
            },
            {
                "tag": "EDA",
                "title": "EDA: Red Bull Sales",
                "desc": "สำรวจข้อมูลยอดขายเชิงภาพผ่านกราฟ interactive เพื่อทำความเข้าใจพฤติกรรมข้อมูล",
                "page": "pages/EDA_app.py",
            },
        ],
    },
    {
        "code": "04",
        "title": "Machine Learning",
        "sub": "พยากรณ์ จำแนก และจัดกลุ่มข้อมูลจาก use case ที่เข้าใจง่ายและต่อยอดได้จริง",
        "apps": [
            {
                "tag": "CLASSIFY",
                "title": "High Sales Predictor",
                "desc": "ทำนายว่ายอดขายมีแนวโน้มสูงหรือไม่จากตัวแปรสำคัญทางธุรกิจ",
                "page": "pages/classify_redbull_sale.py",
            },
            {
                "tag": "FORECAST",
                "title": "Sales Prediction App",
                "desc": "พยากรณ์ยอดขายจากข้อมูลเชิงธุรกิจ พร้อมใช้งานในรูปแบบ prototype",
                "page": "pages/sale_predict.py",
            },
            {
                "tag": "OPS",
                "title": "Logistics Service Time",
                "desc": "ทำนายเวลาขนส่งเพื่อช่วยมองเห็นปัจจัยที่มีผลต่อการให้บริการ",
                "page": "pages/truck_predict.py",
            },
            {
                "tag": "SEGMENT",
                "title": "Market Segmentation",
                "desc": "จัดกลุ่มลูกค้าจากรูปแบบข้อมูลเพื่อช่วยวิเคราะห์พฤติกรรมและมูลค่า",
                "page": "pages/clustering_segment.py",
            },
        ],
    },
]

TOTAL_APPS = sum(len(section["apps"]) for section in SECTIONS)

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="topbar">
        <div class="brand-wrap">
            <div class="brand-badge">DS PLAY</div>
            <div class="brand-copy">
                <div class="brand-title">Data Science & Machine Learning Bootcamp</div>
                <div class="brand-sub">Nintendo-inspired learning portal · clean, playful, executive-friendly</div>
            </div>
        </div>
        <div class="nav-links">
            <span class="nav-link">Explore</span>
            <span class="nav-link">Modules</span>
            <span class="nav-link">Projects</span>
            <span class="nav-link">Workshop</span>
        </div>
    </div>

    <div class="hero">
        <div class="hero-inner">
            <div class="hero-kicker">🎮 7-Day Intensive Hands-on Workshop</div>
            <h1>Learn data skills<br>through mini apps.</h1>
            <p>
                ศูนย์รวมแบบฝึกหัดและ prototype สำหรับ Data Science และ Machine Learning
                ที่ออกแบบใหม่ให้ดูสะอาดขึ้น ใช้งานง่ายขึ้น และมี visual hierarchy แบบ Nintendo-inspired
                โดยยังเข้าถึงทุกหน้าเรียนได้จากหน้าหลักเดียว.
            </p>
            <div class="hero-tags">
                <span class="hero-tag">14 mini apps</span>
                <span class="hero-tag">4 learning tracks</span>
                <span class="hero-tag alt">by Ruthapoom</span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="metrics">
        <div class="metric"><div class="metric-no">7</div><div class="metric-label">Workshop Days</div></div>
        <div class="metric"><div class="metric-no">{len(SECTIONS)}</div><div class="metric-label">Learning Tracks</div></div>
        <div class="metric"><div class="metric-no">{TOTAL_APPS}</div><div class="metric-label">Interactive Apps</div></div>
        <div class="metric"><div class="metric-no">DS/ML</div><div class="metric-label">Hands-on Practice</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Section rendering
# ----------------------------------------------------------------------------
for section in SECTIONS:
    st.markdown(
        f"""
        <div class="section-wrap">
            <div class="section-head">
                <div class="section-left">
                    <div class="section-no">{section['code']}</div>
                    <div>
                        <h2 class="section-title">{section['title']}</h2>
                        <p class="section-sub">{section['sub']}</p>
                    </div>
                </div>
                <div class="section-pill">{len(section['apps'])} apps</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    apps = section["apps"]
    cols_per_row = min(4, len(apps))
    for start in range(0, len(apps), cols_per_row):
        row_apps = apps[start:start + cols_per_row]
        cols = st.columns(cols_per_row, gap="medium")
        for col, app in zip(cols, row_apps):
            with col:
                st.markdown(
                    f"""
                    <div class="app-card">
                        <div>
                            <div class="app-top">
                                <span class="app-code">{app['tag']}</span>
                                <span class="app-type">Mini App</span>
                            </div>
                            <div class="app-title">{app['title']}</div>
                            <p class="app-desc">{app['desc']}</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button("Open app", key=app["page"]):
                    st.switch_page(app["page"])

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### DS PLAY")
    st.caption("Learning portal")
    st.markdown(
        """
        <div class="side-panel">
            <span class="side-badge">BOOTCAMP</span>
            <div class="side-heading">Data Science & ML</div>
            <div class="side-copy">
                เลือกเรียนทีละหัวข้อจาก Day 1 → Data Cleaning → EDA → Machine Learning
                เพื่อค่อย ๆ สร้างความเข้าใจจากพื้นฐานไปสู่การประยุกต์ใช้งานจริง.
            </div>
        </div>
        <div class="side-panel">
            <div class="side-heading">Design direction</div>
            <div class="side-copy">
                เน้น white space, typography ชัด, card ที่อ่านง่าย, CTA ที่เด่น และเลย์เอาต์ที่ไม่ดูรกเกินไป.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("Made by **Ruthapoom**")
