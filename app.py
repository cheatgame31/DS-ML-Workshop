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
# Theme & styling
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sarabun:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', 'Sarabun', sans-serif;
        }

        /* ซ่อน element รก ๆ ของ Streamlit */
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .block-container { padding-top: 2.5rem; max-width: 1180px; }

        /* ---------- Hero ---------- */
        .hero {
            background:
                radial-gradient(1200px 400px at 10% -20%, rgba(124,58,237,0.45), transparent),
                radial-gradient(900px 400px at 100% 0%, rgba(37,99,235,0.45), transparent),
                linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
            padding: 3rem 2.5rem;
            border-radius: 24px;
            color: #fff;
            margin-bottom: 0.5rem;
            box-shadow: 0 20px 50px rgba(49, 46, 129, 0.35);
        }
        .hero .eyebrow {
            display: inline-block;
            background: rgba(255,255,255,0.14);
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            margin-bottom: 1rem;
        }
        .hero h1 {
            font-size: 2.7rem;
            line-height: 1.15;
            margin: 0;
            font-weight: 800;
            letter-spacing: -0.02em;
        }
        .hero p { font-size: 1.05rem; margin-top: 0.7rem; opacity: 0.85; max-width: 640px; }

        /* ---------- Section heading ---------- */
        .sec {
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #7c3aed;
            margin: 2.2rem 0 1rem 0.2rem;
        }

        /* ---------- Cards (buttons) ---------- */
        div[data-testid="stVerticalBlock"] div.stButton > button {
            width: 100%;
            min-height: 132px;
            padding: 1.2rem 1.3rem;
            border-radius: 18px;
            border: 1px solid rgba(0,0,0,0.06);
            background: #ffffff;
            box-shadow: 0 2px 8px rgba(16,24,40,0.05);
            text-align: left;
            white-space: pre-line;
            line-height: 1.4;
            font-family: 'Inter', 'Sarabun', sans-serif;
            transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
        }
        div[data-testid="stVerticalBlock"] div.stButton > button:hover {
            transform: translateY(-4px);
            border-color: rgba(124,58,237,0.55);
            box-shadow: 0 16px 34px rgba(124,58,237,0.18);
        }
        div[data-testid="stVerticalBlock"] div.stButton > button:active { transform: translateY(-1px); }
        div[data-testid="stVerticalBlock"] div.stButton > button:focus { box-shadow: 0 16px 34px rgba(124,58,237,0.18); }

        /* ปรับสำหรับ dark theme */
        @media (prefers-color-scheme: dark) {
            div[data-testid="stVerticalBlock"] div.stButton > button {
                background: #1a1a23;
                border-color: rgba(255,255,255,0.08);
            }
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
        <span class="eyebrow">7-DAY INTENSIVE WORKSHOP</span>
        <h1>Data Science &amp;<br>Machine Learning Bootcamp</h1>
        <p>รวมแอปพลิเคชันทั้งหมดจากเวิร์กชอป — เลือกหัวข้อที่ต้องการเพื่อเริ่มใช้งานได้ทันที</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# โครงสร้างเมนู
# ----------------------------------------------------------------------------
SECTIONS = [
    {
        "label": "Day 1 · Python Foundations",
        "apps": [
            ("💰", "คำนวณส่วนลด", "คำนวณส่วนลดตามยอดซื้อของลูกค้า", "pages/app1_discount_calc.py"),
            ("📦", "วิเคราะห์คลังสินค้า", "สรุปมูลค่าสต๊อกและสินค้าที่ต้องสั่งซื้อ", "pages/energy_inventory.py"),
        ],
    },
    {
        "label": "Data Cleaning",
        "apps": [
            ("📂", "Customer Data Cleaner", "ทำความสะอาดข้อมูลลูกค้า", "pages/clean_customers.py"),
            ("🐂", "Cleaning Workshop", "เวิร์กชอปทำความสะอาดข้อมูล", "pages/clean_app.py"),
            ("🥤", "Energy Drink Cleaning", "เคลียร์ข้อมูลยอดขายเครื่องดื่ม", "pages/clean_energy_drink_sales.py"),
            ("🧼", "My Clean Data App", "เครื่องมือทำความสะอาดข้อมูลทั่วไป", "pages/test.py"),
        ],
    },
    {
        "label": "Transform & EDA",
        "apps": [
            ("🛠️", "Data Transformation", "แปลงและปรับรูปแบบข้อมูล", "pages/transform_app.py"),
            ("💡", "EDA · Red Bull Sales", "สำรวจและวิเคราะห์ข้อมูลเชิงลึก", "pages/EDA_app.py"),
        ],
    },
    {
        "label": "Machine Learning",
        "apps": [
            ("🎯", "High Sales Predictor", "จำแนกสินค้าขายดีด้วยโมเดล ML", "pages/classify_redbull_sale.py"),
            ("📈", "Sales Prediction", "พยากรณ์ยอดขายล่วงหน้า", "pages/sale_predict.py"),
            ("🚛", "Logistics Prediction", "ทำนายเวลาบริการและจัดตารางขนส่ง", "pages/truck_predict.py"),
        ],
    },
]

COLS_PER_ROW = 3

for section in SECTIONS:
    st.markdown(f'<div class="sec">{section["label"]}</div>', unsafe_allow_html=True)
    apps = section["apps"]
    for i in range(0, len(apps), COLS_PER_ROW):
        row = apps[i : i + COLS_PER_ROW]
        cols = st.columns(COLS_PER_ROW, gap="medium")
        for col, (emoji, title, desc, page) in zip(cols, row):
            with col:
                if st.button(f"{emoji}\n\n{title}\n{desc}", key=page):
                    st.switch_page(page)

# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.caption("Made with ❤️ by Ruthapoom · DS & ML Bootcamp")
