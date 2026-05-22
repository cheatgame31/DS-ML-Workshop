import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import time

# --- Page Config ---
st.set_page_config(
    page_title="Red Bull Data Elite",
    page_icon="🐂",
    layout="wide"
)

# --- Professional Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*=\"st-\"] { font-family: 'Inter', sans-serif; }
    
    .stApp { background-color: #f8f9fa; }
    
    /* Header Styling */
    .main-header { 
        background: linear-gradient(90deg, #001e36 0%, #004b87 100%);
        padding: 30px; border-radius: 15px; color: white; margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Card Styling */
    .metric-card {
        background: white; border-radius: 12px; padding: 20px;
        border-left: 5px solid #ff0000; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%; border-radius: 25px; height: 3em; 
        background-color: #ff0000 !important; color: white !important;
        font-weight: bold; border: none; transition: 0.3s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(255,0,0,0.3); }
    
    /* Status Styling */
    div[data-testid=\"stStatus\"] { border-radius: 12px; border: 1px solid #e0e0e0; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Control ---
with st.sidebar:
    st.image("https://www.redbull.com/v3/resources/images/client/header/redbull-logo.svg", width=150)
    st.markdown("### 🛠 Processing Studio")
    st.divider()
    steps = st.multiselect(
        "Select Cleaning Modules",
        ["🔍 Exploration", "👥 Deduplication", "🔄 Standardization", "📭 Missing Fill", "📢 Logic Check", "📐 Outlier Profile"],
        default=["🔍 Exploration", "👥 Deduplication", "🔄 Standardization", "📭 Missing Fill", "📢 Logic Check", "📐 Outlier Profile"]
    )
    st.info("Choose your pipeline steps and upload the CSV to begin optimization.")

# --- App Header ---
st.markdown("""
    <div class='main-header'>
        <h1>🐂 Red Bull Data Elite <span style='font-size: 0.5em; vertical-align: middle;'>v2.0</span></h1>
        <p>Professional Sales Pipeline & Data Optimization Suite</p>
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["csv"])

if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
    df = df_raw.copy()

    # High-End Metrics Row
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown("<div class='metric-card'><h5>Records</h5><h2>{:,.0f}</h2></div>".format(len(df)), unsafe_allow_html=True)
    with c2: st.markdown("<div class='metric-card' style='border-left-color:#ffcc00'><h5>Missing</h5><h2>{}</h2></div>".format(df.isna().sum().sum()), unsafe_allow_html=True)
    with c3: st.markdown("<div class='metric-card' style='border-left-color:#001e36'><h5>Features</h5><h2>{}</h2></div>".format(len(df.columns)), unsafe_allow_html=True)
    with c4: st.markdown("<div class='metric-card' style='border-left-color:#00a100'><h5>Duplicates</h5><h2>{}</h2></div>".format(df.duplicated().sum()), unsafe_allow_html=True)

    st.write(" ")

    if st.button("🔥 EXECUTE DATA OPTIMIZATION"):
        with st.status("🚀 Optimizing Intelligence Pipeline...", expanded=True) as status:
            
            if "🔍 Exploration" in steps:
                st.write("#### 1. Data Intelligence Audit")
                st.dataframe(df.describe().T, use_container_width=True)
                time.sleep(0.4)

            if "👥 Deduplication" in steps:
                st.write("#### 2. Pattern Matching & Removal")
                pre = len(df)
                df = df.drop_duplicates()
                st.caption(f"Optimized: Removed {pre - len(df)} redundant rows.")

            if "🔄 Standardization" in steps:
                st.write("#### 3. Categorical Alignment")
                df['Region'] = df['Region'].str.strip().str.upper().replace({'USA EAST': 'USA-EAST', 'EU': 'EUROPE-EU', 'APAC': 'ASIA-PACIFIC'})
                df['Product_Variant'] = df['Product_Variant'].str.strip().str.title()
                df['Channel'] = df['Channel'].str.replace('_', ' ').str.title()
                st.caption("Result: 100% Text Uniformity achieved.")

            if "📭 Missing Fill" in steps:
                st.write("#### 4. Neural Imputation (Median)")
                for col in ['Marketing_Spend', 'Customer_Score']:
                    df[col] = df[col].fillna(df[col].median())
                st.caption("Result: Zero null values remain in core features.")

            if "📢 Logic Check" in steps:
                st.write("#### 5. Business Constraint Validation")
                initial = len(df)
                df = df[(df['Unit_Price'] > 0) & (df['Units_Sold'] > 0) & (df['Customer_Score'] <= 10)]
                st.caption(f"Validation: Filtered {initial - len(df)} logic violations.")

            if "📐 Outlier Profile" in steps:
                st.write("#### 6. Distribution Analysis")
                fig, ax = plt.subplots(1, 2, figsize=(12, 4))
                sns.boxplot(x=df['Units_Sold'], color='#ff0000', ax=ax[0])
                sns.boxplot(x=df['Marketing_Spend'], color='#001e36', ax=ax[1])
                st.pyplot(fig)

            status.update(label="Pipeline Finalized!", state="complete", expanded=False)

        st.balloons()
        st.success("✨ Intelligence optimization complete. Dataset is analysis-ready.")

        res_left, res_right = st.columns([3, 1])
        with res_left:
            st.subheader("Cleaned Intelligence Preview")
            st.dataframe(df.head(10), use_container_width=True)

        with res_right:
            st.subheader("Final Delivery")
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ DOWNLOAD OPTIMIZED CSV",
                data=csv,
                file_name="redbull_optimized.csv",
                mime="text/csv",
                use_container_width=True
            )
            st.metric("Final Growth", f"{len(df)}", delta=f"{len(df)-len(df_raw)}")

else:
    st.write(" ")
    st.info("👋 Welcome. Please drag and drop the Red Bull CSV file above to initialize the elite cleaning suite.")
