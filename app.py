import streamlit as st

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="DS & ML Bootcamp",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Custom styling
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        /* ซ่อน footer "Made with Streamlit" */
        footer {visibility: hidden;}

        .hero {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            padding: 2.5rem 2rem;
            border-radius: 18px;
            color: white;
            text-align: center;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 30px rgba(37, 117, 252, 0.25);
        }
        .hero h1 { font-size: 2.6rem; margin: 0; font-weight: 800; }
        .hero p  { font-size: 1.1rem; margin-top: 0.5rem; opacity: 0.95; }

        .section-title {
            font-size: 1.35rem;
            font-weight: 700;
            margin: 1.6rem 0 0.4rem 0;
            padding-left: 0.6rem;
            border-left: 5px solid #2575fc;
        }
        .section-sub { color: #8a8a8a; margin: 0 0 0.8rem 0.7rem; font-size: 0.92rem; }

        /* ทำให้ปุ่มทุกอันสูงเท่ากัน ดูเป็น card */
        div.stButton > button {
            width: 100%;
            min-height: 90px;
            border-radius: 14px;
            border: 1px solid rgba(37, 117, 252, 0.25);
            font-size: 1.02rem;
            font-weight: 600;
            white-space: normal;
            line-height: 1.35;
            transition: all 0.18s ease-in-out;
            background: var(--background-color);
        }
        div.stButton > button:hover {
            border-color: #2575fc;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(37, 117, 252, 0.22);
            color: #2575fc;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Hero header
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>🚀 Data Science & Machine Learning Bootcamp</h1>
        <p>7 Day Intensive Hands-on Workshop&nbsp;·&nbsp;by <b>Ruthapoom</b></p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# โครงสร้างเมนู: (label, page path, emoji)
# ----------------------------------------------------------------------------
SECTIONS = [
    {
        "title": "🐍 Day 1 · Python & การจัดการข้อมูลพื้นฐาน",
        "sub": "พื้นฐานโครงสร้างข้อมูลและการคำนวณด้วย Python",
        "apps": [
            ("ระบบคำนวณส่วนลดตามยอดซื้อ", "pages/app1_discount_calc.py", "💰"),
            ("ระบบวิเคราะห์คลังสินค้า", "pages/energy_inventory.py", "📦"),
        ],
    },
    {
        "title": "🧹 Data Cleaning · การทำความสะอาดข้อมูล",
        "sub": "จัดการข้อมูลดิบให้พร้อมใช้งาน",
        "apps": [
            ("Customer Data Cleaner", "pages/clean_customers.py", "📂"),
            ("Data Cleaning Workshop", "pages/clean_app.py", "🐂"),
            ("Energy Drink Sales Cleaning", "pages/clean_energy_drink_sales.py", "🥤"),
            ("My App Clean Data", "pages/test.py", "🧼"),
        ],
    },
    {
        "title": "🛠️ Transform & EDA · แปลงและสำรวจข้อมูล",
        "sub": "Data Transformation และ Exploratory Data Analysis",
        "apps": [
            ("Data Transformation App", "pages/transform_app.py", "🛠️"),
            ("EDA: Red Bull Sales", "pages/EDA_app.py", "💡"),
        ],
    },
    {
        "title": "🤖 Machine Learning · พยากรณ์และจำแนกข้อมูล",
        "sub": "โมเดลทำนายยอดขายและการจัดตารางขนส่ง",
        "apps": [
            ("Red Bull High Sales Predictor", "pages/classify_redbull_sale.py", "🎯"),
            ("Sales Prediction App", "pages/sale_predict.py", "📈"),
            ("Logistics Service Time Prediction", "pages/truck_predict.py", "🚛"),
        ],
    },
]

# ----------------------------------------------------------------------------
# Render เมนูแบบ grid 3 คอลัมน์
# ----------------------------------------------------------------------------
COLS_PER_ROW = 3

for section in SECTIONS:
    st.markdown(f'<div class="section-title">{section["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-sub">{section["sub"]}</div>', unsafe_allow_html=True)

    apps = section["apps"]
    for i in range(0, len(apps), COLS_PER_ROW):
        row = apps[i : i + COLS_PER_ROW]
        cols = st.columns(COLS_PER_ROW)
        for col, (label, page, emoji) in zip(cols, row):
            with col:
                if st.button(f"{emoji}\n\n{label}", key=page):
                    st.switch_page(page)

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🚀 DS & ML Bootcamp")
    st.caption("เลือกแอปจากหน้าหลัก หรือเมนูด้านล่าง")
    st.divider()
    st.info("7 Day Intensive Hands-on Workshop")
    st.markdown("Made with ❤️ by **Ruthapoom**")
