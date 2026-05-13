import streamlit as st

st.set_page_config(
    page_title="MyApp",
    page_icon="🏠",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .hero-card {
        background: linear-gradient(135deg, #1f77ff 0%, #00b4d8 100%);
        padding: 40px;
        border-radius: 24px;
        color: white;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        margin-bottom: 28px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 22px;
        font-weight: 400;
        opacity: 0.95;
    }

    .info-card {
        background-color: white;
        padding: 26px;
        border-radius: 20px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        border-left: 6px solid #1f77ff;
        margin-bottom: 20px;
    }

    .info-title {
        font-size: 24px;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 8px;
    }

    .info-text {
        font-size: 18px;
        color: #4b5563;
    }

    .menu-card {
        background-color: white;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.07);
        text-align: center;
        min-height: 180px;
    }

    .menu-icon {
        font-size: 46px;
        margin-bottom: 10px;
    }

    .menu-title {
        font-size: 22px;
        font-weight: 700;
        color: #111827;
    }

    .menu-desc {
        font-size: 15px;
        color: #6b7280;
        margin-top: 8px;
    }

    div.stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 14px;
        font-size: 18px;
        font-weight: 700;
        background: linear-gradient(135deg, #1f77ff 0%, #00b4d8 100%);
        color: white;
        border: none;
        margin-top: 14px;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #005bea 0%, #00a6c8 100%);
        color: white;
        border: none;
    }
</style>
""", unsafe_allow_html=True)


# ---------- Hero Section ----------
st.markdown("""
<div class="hero-card">
    <div class="hero-title">🏠 MyApp Learning Portal</div>
    <div class="hero-subtitle">Boot Camp: Data Science and Machine Learning</div>
</div>
""", unsafe_allow_html=True)


# ---------- Course Info ----------
st.markdown("""
<div class="info-card">
    <div class="info-title">📘 7 Day Intensive Hands-on Workshop</div>
    <div class="info-text">
        Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- Menu Section ----------
st.write("### 🚀 เมนูการเรียนรู้")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">💰</div>
        <div class="menu-title">ระบบคำนวณส่วนลด</div>
        <div class="menu-desc">
            คำนวณส่วนลดตามยอดซื้อ และแสดงยอดชำระสุทธิ
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("เปิดระบบคำนวณส่วนลด"):
        st.switch_page("pages/app1_discount_calc.py")

with col2:
    st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">📊</div>
        <div class="menu-title">Data Structure</div>
        <div class="menu-desc">
            เรียนรู้ List, Tuple, Dictionary และ Set
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.button("Coming Soon", disabled=True)

with col3:
    st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">🤖</div>
        <div class="menu-title">Machine Learning</div>
        <div class="menu-desc">
            เตรียมเข้าสู่พื้นฐาน AI และ Machine Learning
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.button("Coming Soon ", disabled=True)


# ---------- Footer ----------
st.markdown("---")
st.caption("© Boot Camp: Data Science and Machine Learning | Created with Streamlit")
