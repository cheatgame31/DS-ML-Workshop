import streamlit as st

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="DS & ML Bootcamp",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Custom styling: Nintendo.com inspired theme
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Sarabun:wght@400;500;600;700;800&display=swap');

        :root {
            --n-red: #e60012;
            --n-red-dark: #bf0010;
            --n-ink: #1f1f1f;
            --n-muted: #6b7280;
            --n-line: #e5e7eb;
            --n-soft: #f7f7f8;
            --n-card: #ffffff;
            --n-yellow: #ffd84d;
            --n-blue: #00a3e0;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', 'Sarabun', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 12% 10%, rgba(230, 0, 18, 0.08), transparent 26%),
                radial-gradient(circle at 88% 18%, rgba(0, 163, 224, 0.08), transparent 24%),
                linear-gradient(180deg, #ffffff 0%, #f7f7f8 100%);
            color: var(--n-ink);
        }

        footer, #MainMenu, header { visibility: hidden; }
        .block-container {
            max-width: 1180px;
            padding-top: 1.35rem;
            padding-bottom: 3rem;
        }

        /* Top navigation */
        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            background: #ffffff;
            border: 1px solid var(--n-line);
            border-radius: 999px;
            padding: 0.65rem 0.8rem 0.65rem 0.7rem;
            box-shadow: 0 8px 24px rgba(17, 24, 39, 0.06);
            margin-bottom: 1rem;
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 0.7rem;
            font-weight: 900;
            letter-spacing: -0.03em;
        }
        .brand-badge {
            background: var(--n-red);
            color: white;
            border-radius: 999px;
            padding: 0.34rem 0.9rem;
            font-size: 0.98rem;
            box-shadow: inset 0 -2px 0 rgba(0,0,0,0.16);
        }
        .nav-pills {
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
            justify-content: flex-end;
        }
        .nav-pill {
            border: 1px solid var(--n-line);
            border-radius: 999px;
            padding: 0.38rem 0.72rem;
            font-size: 0.82rem;
            color: #374151;
            background: #fff;
            font-weight: 700;
        }

        /* Hero */
        .hero {
            position: relative;
            overflow: hidden;
            background: var(--n-red);
            color: white;
            border-radius: 28px;
            padding: 2.45rem 2.2rem;
            border: 1px solid rgba(255,255,255,0.35);
            box-shadow: 0 18px 44px rgba(230, 0, 18, 0.25);
            margin-bottom: 1.1rem;
        }
        .hero::before {
            content: "";
            position: absolute;
            inset: auto -9rem -10rem auto;
            width: 28rem;
            height: 28rem;
            border-radius: 50%;
            background: rgba(255,255,255,0.15);
        }
        .hero::after {
            content: "";
            position: absolute;
            top: -4rem;
            right: 8rem;
            width: 10rem;
            height: 10rem;
            border-radius: 50%;
            border: 26px solid rgba(255,255,255,0.12);
        }
        .hero-content { position: relative; z-index: 2; max-width: 760px; }
        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.28);
            border-radius: 999px;
            padding: 0.4rem 0.75rem;
            font-weight: 800;
            font-size: 0.82rem;
            margin-bottom: 0.85rem;
        }
        .hero h1 {
            font-size: clamp(2.15rem, 5vw, 4.2rem);
            line-height: 0.96;
            margin: 0;
            font-weight: 900;
            letter-spacing: -0.065em;
        }
        .hero p {
            max-width: 620px;
            margin: 1rem 0 0 0;
            font-size: 1.05rem;
            line-height: 1.65;
            opacity: 0.94;
            font-weight: 500;
        }
        .hero-actions {
            margin-top: 1.25rem;
            display: flex;
            flex-wrap: wrap;
            gap: 0.7rem;
        }
        .hero-chip {
            background: #ffffff;
            color: var(--n-red);
            border-radius: 999px;
            padding: 0.52rem 0.9rem;
            font-weight: 900;
            font-size: 0.88rem;
        }
        .hero-chip.dark {
            background: rgba(0,0,0,0.18);
            color: #ffffff;
            border: 1px solid rgba(255,255,255,0.3);
        }

        /* Stats */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.85rem;
            margin: 1rem 0 1.4rem 0;
        }
        .stat-card {
            background: #ffffff;
            border: 1px solid var(--n-line);
            border-radius: 22px;
            padding: 1rem;
            box-shadow: 0 8px 24px rgba(17, 24, 39, 0.05);
        }
        .stat-num {
            font-size: 1.7rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            color: var(--n-red);
        }
        .stat-label {
            color: var(--n-muted);
            font-size: 0.86rem;
            font-weight: 700;
            margin-top: 0.15rem;
        }

        /* Section header */
        .section-head {
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 1rem;
            margin: 1.6rem 0 0.75rem 0;
        }
        .section-title-wrap { display: flex; gap: 0.8rem; align-items: center; }
        .section-icon {
            width: 42px;
            height: 42px;
            border-radius: 14px;
            display: grid;
            place-items: center;
            background: var(--n-red);
            color: #fff;
            font-weight: 900;
            box-shadow: 0 8px 18px rgba(230, 0, 18, 0.22);
        }
        .section-title {
            font-size: 1.35rem;
            line-height: 1.1;
            font-weight: 900;
            letter-spacing: -0.035em;
            margin: 0;
        }
        .section-sub {
            margin: 0.28rem 0 0 0;
            color: var(--n-muted);
            font-size: 0.92rem;
            font-weight: 600;
        }
        .section-count {
            color: var(--n-muted);
            font-size: 0.82rem;
            font-weight: 800;
            border: 1px solid var(--n-line);
            border-radius: 999px;
            padding: 0.34rem 0.65rem;
            background: #fff;
        }

        /* Streamlit button card */
        div.stButton > button {
            position: relative;
            width: 100%;
            min-height: 118px;
            border-radius: 22px;
            border: 1px solid #dedede;
            background: #ffffff;
            color: #1f1f1f;
            font-size: 1rem;
            font-weight: 850;
            line-height: 1.25;
            white-space: pre-line;
            text-align: left;
            padding: 1rem 1.1rem;
            box-shadow: 0 7px 18px rgba(17, 24, 39, 0.06);
            transition: all 0.15s ease;
        }
        div.stButton > button::before {
            content: "Launch";
            position: absolute;
            right: 0.9rem;
            bottom: 0.75rem;
            color: #fff;
            background: var(--n-red);
            border-radius: 999px;
            padding: 0.25rem 0.58rem;
            font-size: 0.72rem;
            font-weight: 900;
            box-shadow: inset 0 -2px 0 rgba(0,0,0,0.16);
        }
        div.stButton > button:hover {
            border-color: var(--n-red);
            transform: translateY(-3px);
            box-shadow: 0 14px 30px rgba(230, 0, 18, 0.15);
            color: var(--n-red);
        }
        div.stButton > button:active {
            transform: translateY(-1px) scale(0.99);
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid var(--n-line);
        }
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: var(--n-red);
            font-weight: 900;
            letter-spacing: -0.03em;
        }
        .side-card {
            border: 1px solid var(--n-line);
            background: #fff;
            border-radius: 18px;
            padding: 0.9rem;
            margin: 0.75rem 0;
            box-shadow: 0 8px 22px rgba(17, 24, 39, 0.04);
        }
        .side-title { font-weight: 900; color: #111827; margin-bottom: 0.2rem; }
        .side-text { font-size: 0.86rem; color: var(--n-muted); line-height: 1.5; }
        .tiny-red {
            display: inline-block;
            background: var(--n-red);
            color: white;
            border-radius: 999px;
            padding: 0.25rem 0.55rem;
            font-size: 0.74rem;
            font-weight: 900;
            margin-bottom: 0.55rem;
        }

        @media (max-width: 900px) {
            .topbar { align-items: flex-start; border-radius: 24px; flex-direction: column; }
            .stats-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .section-head { align-items: flex-start; flex-direction: column; }
        }
        @media (max-width: 520px) {
            .stats-grid { grid-template-columns: 1fr; }
            .hero { padding: 1.8rem 1.35rem; border-radius: 24px; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Menu structure: (label, page path, code)
# ----------------------------------------------------------------------------
SECTIONS = [
    {
        "code": "01",
        "title": "Day 1 · Python & Data Basics",
        "sub": "พื้นฐานโครงสร้างข้อมูล การคำนวณ และการคิดแบบ data-driven",
        "apps": [
            ("Discount Calculator\nระบบคำนวณส่วนลดตามยอดซื้อ", "pages/app1_discount_calc.py", "SHOP"),
            ("Inventory Analytics\nระบบวิเคราะห์คลังสินค้า", "pages/energy_inventory.py", "DATA"),
        ],
    },
    {
        "code": "02",
        "title": "Data Cleaning",
        "sub": "จัดการข้อมูลดิบ Missing, Duplicate และ Format ให้พร้อมใช้งาน",
        "apps": [
            ("Customer Data Cleaner\nเตรียมข้อมูลลูกค้า", "pages/clean_customers.py", "CLEAN"),
            ("Data Cleaning Workshop\nแบบฝึกหัดทำความสะอาดข้อมูล", "pages/clean_app.py", "LAB"),
            ("Energy Drink Sales Cleaning\nทำความสะอาดข้อมูลยอดขาย", "pages/clean_energy_drink_sales.py", "SALE"),
            ("My App Clean Data\nทดลองล้างข้อมูล", "pages/test.py", "TRY"),
        ],
    },
    {
        "code": "03",
        "title": "Transform & EDA",
        "sub": "แปลงข้อมูล สำรวจ Pattern และสร้าง Insight จากกราฟ",
        "apps": [
            ("Data Transformation App\nแปลงข้อมูลเพื่อวิเคราะห์", "pages/transform_app.py", "FLOW"),
            ("EDA: Red Bull Sales\nสำรวจยอดขายเชิงภาพ", "pages/EDA_app.py", "CHART"),
        ],
    },
    {
        "code": "04",
        "title": "Machine Learning",
        "sub": "พยากรณ์ จำแนก และต่อยอดเป็น prototype สำหรับธุรกิจ",
        "apps": [
            ("High Sales Predictor\nทำนายยอดขายสูง", "pages/classify_redbull_sale.py", "ML"),
            ("Sales Prediction App\nพยากรณ์ยอดขาย", "pages/sale_predict.py", "PRED"),
            ("Logistics Service Time\nทำนายเวลาขนส่ง", "pages/truck_predict.py", "OPS"),
            ("Market Segmentation\nจัดกลุ่มลูกค้า", "pages/clustering_segment.py", "SEG"),
        ],
    },
]

TOTAL_APPS = sum(len(section["apps"]) for section in SECTIONS)

# ----------------------------------------------------------------------------
# Topbar + Hero
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            <span class="brand-badge">DS PLAY</span>
            <span>Data Science & ML Bootcamp</span>
        </div>
        <div class="nav-pills">
            <span class="nav-pill">Explore</span>
            <span class="nav-pill">Workshops</span>
            <span class="nav-pill">Projects</span>
            <span class="nav-pill">Support</span>
        </div>
    </div>

    <div class="hero">
        <div class="hero-content">
            <div class="eyebrow">🎮 7-Day Hands-on Learning Portal</div>
            <h1>Learn Data.<br>Build Models.<br>Play with Insight.</h1>
            <p>
                รวมแอปฝึกปฏิบัติสำหรับ Data Science และ Machine Learning
                ในรูปแบบ learning hub ที่เข้าใจง่าย ใช้งานเร็ว และดูเป็น production มากขึ้น
            </p>
            <div class="hero-actions">
                <span class="hero-chip">Start learning</span>
                <span class="hero-chip dark">by Ruthapoom</span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="stats-grid">
        <div class="stat-card"><div class="stat-num">7</div><div class="stat-label">Day Workshop</div></div>
        <div class="stat-card"><div class="stat-num">{len(SECTIONS)}</div><div class="stat-label">Learning Tracks</div></div>
        <div class="stat-card"><div class="stat-num">{TOTAL_APPS}</div><div class="stat-label">Mini Apps</div></div>
        <div class="stat-card"><div class="stat-num">ML</div><div class="stat-label">Hands-on Projects</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Render menu grid
# ----------------------------------------------------------------------------
COLS_PER_ROW = 3

for section in SECTIONS:
    st.markdown(
        f"""
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">{section['code']}</div>
                <div>
                    <h2 class="section-title">{section['title']}</h2>
                    <p class="section-sub">{section['sub']}</p>
                </div>
            </div>
            <div class="section-count">{len(section['apps'])} apps</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    apps = section["apps"]
    for i in range(0, len(apps), COLS_PER_ROW):
        row = apps[i : i + COLS_PER_ROW]
        cols = st.columns(COLS_PER_ROW, gap="medium")
        for col, (label, page, tag) in zip(cols, row):
            with col:
                if st.button(f"{tag}\n\n{label}", key=page):
                    st.switch_page(page)

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### DS PLAY")
    st.caption("Nintendo.com inspired learning portal")
    st.divider()
    st.markdown(
        """
        <div class="side-card">
            <span class="tiny-red">BOOTCAMP</span>
            <div class="side-title">Data Science & ML</div>
            <div class="side-text">
                เลือกแอปจากหน้าหลักเพื่อเริ่มฝึกทีละ module
                ตั้งแต่ Data Cleaning, EDA ไปจนถึง Machine Learning
            </div>
        </div>
        <div class="side-card">
            <div class="side-title">Design direction</div>
            <div class="side-text">
                Clean white space, rounded cards, strong red CTA,
                playful but controlled visual hierarchy.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("Made by **Ruthapoom**")
