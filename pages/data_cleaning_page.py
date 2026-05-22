import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Red Bull Data Cleaning Pro",
    page_icon="🐂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Minimal Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #FF4B4B; color: white; }
    .stExpander { border: none !important; box-shadow: none !important; background-color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/RedBullEnergyDrink.svg/1200px-RedBullEnergyDrink.svg.png", width=80)
    with col2:
        st.title("Red Bull Data Cleaning Dashboard")
        st.caption("A minimal & smart way to prepare your sales dataset for analysis.")

st.divider()

# --- Sidebar Settings ---
st.sidebar.header("🛠 Settings")
cleaning_steps = st.sidebar.multiselect(
    "Select Cleaning Pipeline:",
    ["1. Exploration", "2. Exact Duplicates", "3. Text Standardization", "4. Missing Values", "5. Logic & Noisy Data", "6. Outlier Profile"],
    default=["1. Exploration", "2. Exact Duplicates", "3. Text Standardization", "4. Missing Values", "5. Logic & Noisy Data", "6. Outlier Profile"]
)

# --- Main Logic ---
uploaded_file = st.sidebar.file_uploader("Upload redbull_workshop_dirty.csv", type=["csv"])

if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
    df = df_raw.copy()

    # Display Metrics Before
    st.subheader("📈 Data Overview")
    m1, m2, m3 = st.columns(3)
    m1.metric("Initial Rows", f"{len(df_raw):,}")
    m2.metric("Columns", len(df_raw.columns))
    m3.metric("Missing Fields", df_raw.isna().sum().sum())

    if st.button("🚀 Run Cleaning Pipeline"):
        with st.status("Cleaning in progress...", expanded=True) as status:
            
            # Step 1: Exploration
            if "1. Exploration" in cleaning_steps:
                st.write("### 🔍 Step 1: Data Exploration")
                st.dataframe(df.describe(include='all'), use_container_width=True)

            # Step 2: Duplicates
            if "2. Exact Duplicates" in cleaning_steps:
                st.write("### 👥 Step 2: Handling Duplicates")
                dup_count = df.duplicated().sum()
                df = df.drop_duplicates()
                st.info(f"Removed {dup_count} exact duplicate rows.")

            # Step 3: Text Standardization
            if "3. Text Standardization" in cleaning_steps:
                st.write("### 🔄 Step 3: Text Standardization")
                # Region
                df['Region'] = df['Region'].str.strip().str.upper().replace({
                    'THAI-CENTRAL': 'TH-CENTRAL', 'THAILAND CENTRAL': 'TH-CENTRAL', 'US EAST': 'USA-EAST', 'EU': 'EUROPE-EU'
                })
                # Product
                df['Product_Variant'] = df['Product_Variant'].str.strip().str.title()
                # Channel
                df['Channel'] = df['Channel'].str.strip().str.title().replace({'Tv Ad': 'TV Ad', 'Tv Ads': 'TV Ad', 'Social_Media': 'Social Media'})
                st.success("Standardized 'Region', 'Product_Variant', and 'Channel' columns.")

            # Step 4: Missing Values
            if "4. Missing Values" in cleaning_steps:
                st.write("### 📭 Step 4: Filling Missing Data")
                df['Marketing_Spend'] = df['Marketing_Spend'].fillna(df['Marketing_Spend'].median())
                df['Customer_Score'] = df['Customer_Score'].fillna(df['Customer_Score'].median())
                st.success("Imputed missing values with Medians.")

            # Step 5: Logic Check
            if "5. Logic & Noisy Data" in cleaning_steps:
                st.write("### 📢 Step 5: Logic & Noisy Data")
                initial_count = len(df)
                df = df[(df['Unit_Price'] > 0) & (df['Units_Sold'] > 0) & 
                        (df['Marketing_Spend'] >= 0) & 
                        (df['Customer_Score'] >= 1) & (df['Customer_Score'] <= 10)]
                st.warning(f"Dropped {initial_count - len(df)} rows violating business logic.")

            # Step 6: Outlier Profile
            if "6. Outlier Profile" in cleaning_steps:
                st.write("### 📐 Step 6: Outlier Detection")
                fig, axes = plt.subplots(1, 2, figsize=(12, 4))
                sns.boxplot(x=df['Units_Sold'], ax=axes[0], color='#FF4B4B')
                sns.boxplot(x=df['Marketing_Spend'], ax=axes[1], color='#31333F')
                st.pyplot(fig)

            status.update(label="Data Cleaning Complete!", state="complete", expanded=False)

        st.divider()
        
        # Summary Final
        st.success("✨ Process Finished Successfully!")
        f1, f2 = st.columns(2)
        with f1:
            st.metric("Cleaned Rows", f"{len(df):,}", delta=f"{len(df)-len(df_raw)}")
            st.write("### Clean Data Preview")
            st.dataframe(df.head(10))
        
        with f2:
            st.write("### Export Result")
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Cleaned CSV",
                data=csv,
                file_name="redbull_clean_final.csv",
                mime="text/csv",
            )
            st.image("https://www.redbull.com/v3/resources/images/client/header/redbull-logo.svg", width=150)

else:
    st.info("Please upload your Red Bull dataset from the sidebar to begin ✨")
