import streamlit as st

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

from scipy.stats.mstats import winsorize

import io

import warnings

warnings.filterwarnings('ignore')
 
# --- Page Configuration ---

st.set_page_config(

    page_title="Data Cleaning Workshop App 🐂",

    layout="wide",

    initial_sidebar_state="expanded",

)
 
# --- Custom CSS for a nicer look ---

st.markdown(

    """
<style>

    .main-header {color: #e62020; font-size: 3em; text-align: center;}

    .subheader {color: #1a73e8;}

    .stButton>button {background-color: #4CAF50; color: white;}

    .stDownloadButton>button {background-color: #2196F3; color: white;}
</style>

    """,

    unsafe_allow_html=True

)
 
# --- Streamlit App Title and Introduction ---

st.markdown('<h1 class="main-header">🐂 Data Cleaning Workshop App</h1>', unsafe_allow_html=True)

st.info("ยินดีต้อนรับสู่แอปพลิเคชัน Data Cleaning! อัปโหลดไฟล์ CSV ของคุณเพื่อเริ่มต้น")

st.warning("⚠️ **ข้อควรระวัง:** แอปพลิเคชันนี้ออกแบบมาสำหรับชุดข้อมูลที่มีโครงสร้างใกล้เคียงกับ `redbull_workshop_dirty.csv` เท่านั้น")
 
# --- File Uploader ---

st.markdown("## 📂 อัปโหลดไฟล์ข้อมูลของคุณ")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv", "txt"]) # เพิ่ม .txt เพื่อความยืดหยุ่น
 
if uploaded_file is not None:

    df_raw = pd.read_csv(uploaded_file)

    df = df_raw.copy()

    st.success("✅ อัปโหลดไฟล์สำเร็จ! เริ่มทำความสะอาดข้อมูลได้เลย")
 
    st.markdown("### Raw Data Preview (5 แถวแรก)")

    st.dataframe(df_raw.head())
 
    # --- Data Cleaning Steps (as functions) ---

    @st.cache_data

    def perform_data_exploration(data):

        st.markdown("<h3 class='subheader'>📊 1. Data Exploration</h3>", unsafe_allow_html=True)

        with st.expander("ดูข้อมูลเบื้องต้น", expanded=False):

            st.write("#### Data Shape:")

            st.write(f"**จำนวนแถว:** {data.shape[0]:,} | **จำนวนคอลัมน์:** {data.shape[1]}")
 
            st.write("#### Data Info:")

            buffer = io.StringIO()

            data.info(buf=buffer)

            st.text(buffer.getvalue())
 
            st.write("#### Descriptive Statistics:")

            st.dataframe(data.describe(include='all'))

        return data
 
    @st.cache_data

    def handle_duplicate_data(data):

        st.markdown("<h3 class='subheader'>👥 2. Duplicate Data</h3>", unsafe_allow_html=True)

        with st.spinner("กำลังตรวจสอบข้อมูลซ้ำ..."):

            exact_dups = data.duplicated()

            exact_dup_count = exact_dups.sum()

            if exact_dup_count > 0:

                st.warning(f"พบข้อมูลซ้ำ 100% จำนวน **{exact_dup_count:,}** แถว")

                with st.expander("คลิกเพื่อดูตัวอย่างข้อมูลซ้ำ", expanded=False):

                    st.dataframe(data[exact_dups])

                data = data.drop_duplicates()

                st.success(f"✅ ลบข้อมูลซ้ำแล้ว! เหลือ **{len(data):,}** แถว")

            else:

                st.info("ไม่พบ Exact Duplicate ในข้อมูลนี้ 🎉")

        return data
 
    @st.cache_data

    def handle_inconsistent_data(data):

        st.markdown("<h3 class='subheader'>🔄 3. Inconsistent Data</h3>", unsafe_allow_html=True)

        st.write("##### กำลังแก้ไขค่าที่ไม่สอดคล้องกัน (Standardize & Map)...")
 
        cat_cols = ['Region', 'Product_Variant', 'Channel']

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Unique Values (ก่อนแก้ไข):**")

            for col in cat_cols:

                st.write(f"**📌 {col} ({len(data[col].unique())} ค่า):**")

                st.write(data[col].unique())
 
        # 1. Standardize Region Column

        data['Region'] = data['Region'].str.strip().str.lower()

        region_mapping = {

            'th-central': 'TH-Central', 'th central': 'TH-Central',

            'thailand central': 'TH-Central', 'thailand-central': 'TH-Central',

            'thailand': 'TH-Central',

            'usa-east': 'USA-East', 'us east': 'USA-East',

            'united states east': 'USA-East', 'u.s.a.': 'USA-East',

            'europe-eu': 'Europe-EU', 'eu': 'Europe-EU',

            'europe': 'Europe-EU', 'european union': 'Europe-EU',

            'asia-pacific': 'Asia-Pacific', 'asia-pac': 'Asia-Pacific',

            'apac': 'Asia-Pacific', 'asia pacific': 'Asia-Pacific'

        }

        data['Region'] = data['Region'].replace(region_mapping)

        data['Region'] = data['Region'].str.upper()
 
        # 2. Standardize Product_Variant Column

        data['Product_Variant'] = data['Product_Variant'].str.strip().str.lower()

        product_variant_mapping = {

            'original blue': 'Original Blue', 'original  blue': 'Original Blue',

            'krating daeng 250': 'Krating Daeng 250',

            'red edition': 'Red Edition',

            'sugarfree': 'Sugarfree', 'sugar free': 'Sugarfree',

            'sugarfree ': 'Sugarfree', 'sugar-free': 'Sugarfree',

            'tropical edition': 'Tropical Edition', 'tropical  edition': 'Tropical Edition',

            'tropical': 'Tropical Edition',

        }

        data['Product_Variant'] = data['Product_Variant'].replace(product_variant_mapping)
 
        # 3. Standardize Channel Column

        data['Channel'] = data['Channel'].str.strip().str.lower()

        channel_mapping = {

            'social media': 'Social Media', 'social_media': 'Social Media',

            'tv ad': 'TV Ad', 'tv ads': 'TV Ad',

            'tv advertisement': 'TV Ad', 'television ad': 'TV Ad',

            'in-store promo': 'In-store Promo',

            'f1 sponsorship': 'F1 Sponsorship',

            'extreme sports': 'Extreme Sports'

        }

        data['Channel'] = data['Channel'].replace(channel_mapping)

        data['Channel'] = data['Channel'].apply(lambda x: x.title() if isinstance(x, str) else x)
 
        # Convert Date to datetime

        data['Date'] = pd.to_datetime(data['Date'], format='mixed', errors='coerce') # 'coerce' will turn unparseable dates into NaT

        if data['Date'].isnull().any():

            st.warning("บางค่าในคอลัมน์ 'Date' ไม่สามารถแปลงเป็นวันที่ได้และถูกเปลี่ยนเป็น NaT (Not a Time). โปรดตรวจสอบข้อมูลต้นฉบับ.")
 
 
        st.success("✅ แก้ไข Inconsistent Values สำเร็จแล้ว!")

        with col2:

            st.write("**Unique Values (หลังแก้ไข):**")

            for col in cat_cols:

                st.write(f"**📌 {col} ({len(data[col].unique())} ค่า):**")

                st.write(data[col].unique())
 
        return data
 
    @st.cache_data

    def handle_missing_data(data):

        st.markdown("<h3 class='subheader'>📭 4. Missing Data</h3>", unsafe_allow_html=True)

        missing_count_before = data.isnull().sum()

        if missing_count_before.sum() > 0:

            st.warning("พบ Missing Values ในข้อมูล:")

            with st.expander("คลิกเพื่อดูจำนวน Missing Values ก่อนแก้ไข", expanded=True):

                st.dataframe(missing_count_before[missing_count_before > 0])
 
            st.write("##### กำลังเติม Missing Values...")

            if 'Marketing_Spend' in data.columns and data['Marketing_Spend'].isnull().any():

                median_marketing = data['Marketing_Spend'].median()

                data['Marketing_Spend'] = data['Marketing_Spend'].fillna(median_marketing)

                st.info(f'✅ Marketing_Spend: เติมด้วย Median = **{median_marketing:,.2f}**')
 
            if 'Customer_Score' in data.columns and data['Customer_Score'].isnull().any():

                median_score = data['Customer_Score'].median()

                data['Customer_Score'] = data['Customer_Score'].fillna(median_score)

                st.info(f'✅ Customer_Score: เติมด้วย Median = **{median_score}**')
 
            st.success("✅ แก้ไข Missing Values สำเร็จแล้ว!")

            missing_count_after = data.isnull().sum()

            if missing_count_after.sum() == 0:

                st.info("ไม่มี Missing Values เหลืออยู่แล้ว 🎉")

            else:

                st.warning("ยังคงมี Missing Values หลังจากการแก้ไข:")

                st.dataframe(missing_count_after[missing_count_after > 0])

        else:

            st.info("ไม่พบ Missing Data ในข้อมูลนี้ 🎉")

        return data
 
    @st.cache_data

    def handle_noisy_data(data):

        st.markdown("<h3 class='subheader'>📢 5. Noisy Data</h3>", unsafe_allow_html=True)

        st.write("##### ตรวจสอบและแก้ไขข้อมูลที่ผิดพลาดตาม Business Logic:")
 
        initial_rows = len(data)

        noisy_issues = []
 
        if (data['Unit_Price'] <= 0).any():

            neg_price_count = (data['Unit_Price'] <= 0).sum()

            noisy_issues.append(f"❌ Unit_Price \u2264 0: **{neg_price_count:,}** แถว")
 
        if (data['Units_Sold'] <= 0).any():

            neg_units_count = (data['Units_Sold'] <= 0).sum()

            noisy_issues.append(f"❌ Units_Sold \u2264 0: **{neg_units_count:,}** แถว")
 
        if (data['Marketing_Spend'] < 0).any():

            neg_mkt_count = (data['Marketing_Spend'] < 0).sum()

            noisy_issues.append(f"❌ Marketing_Spend < 0: **{neg_mkt_count:,}** แถว")
 
        if ((data['Customer_Score'] < 1) | (data['Customer_Score'] > 10)).any():

            bad_score_count = ((data['Customer_Score'] < 1) | (data['Customer_Score'] > 10)).sum()

            noisy_issues.append(f"❌ Customer_Score ไม่อยู่ในช่วง 1-10: **{bad_score_count:,}** แถว")
 
        if noisy_issues:

            for issue in noisy_issues:

                st.warning(issue)
 
            st.write("##### กำลังลบแถวที่มี Noisy Data...")

            data = data[data['Unit_Price'] > 0]

            data = data[data['Units_Sold'] > 0]

            data = data[data['Marketing_Spend'] >= 0]

            data = data[(data['Customer_Score'] >= 1) & (data['Customer_Score'] <= 10)]

            rows_removed = initial_rows - len(data)

            st.success(f"✅ แก้ไข Noisy Data สำเร็จแล้ว! ลบไป **{rows_removed:,}** แถว")

        else:

            st.info("ไม่พบ Noisy Data ที่ขัดแย้งกับ Business Logic 🎉")

        return data
 
    @st.cache_data

    def perform_outlier_analysis(data):

        st.markdown("<h3 class='subheader'>📐 6. Outlier Detection & Treatment</h3>", unsafe_allow_html=True)

        st.write("##### ตรวจสอบ Outliers ด้วย Boxplot:")
 
        numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if 'Customer_Score' in numeric_cols:

            numeric_cols.remove('Customer_Score') # Handled in noisy data to be 1-10
 
        if numeric_cols:

            st.info("กำลังสร้าง Boxplots เพื่อแสดง Outliers... (อาจใช้เวลาสักครู่)")

            # Dynamically adjust columns for boxplots

            num_plots = len(numeric_cols)

            if num_plots > 0:

                rows = (num_plots + 1) // 2  # At most 2 plots per row

                fig_height = rows * 3 # Adjust height based on number of rows of plots

                fig = plt.figure(figsize=(15, fig_height))
 
                for i, col in enumerate(numeric_cols):

                    ax = fig.add_subplot(rows, 2, i + 1)

                    sns.boxplot(x=data[col], ax=ax)

                    ax.set_title(f'Boxplot of {col}')

                plt.tight_layout()

                st.pyplot(fig)

                plt.close(fig)
 
            st.markdown("""

            **💡 หมายเหตุเกี่ยวกับการจัดการ Outliers:**

            ใน Workshop นี้ เราได้สังเกตว่าการใช้ `winsorize` หรือการลบ Outliers โดยตรงอาจทำให้ Business Logic ของข้อมูลเปลี่ยนไป (เช่น `Units_Sold` ที่ถูกปรับค่าอาจไม่สะท้อนยอดขายจริง)

            ดังนั้น ในกรณีนี้ เราจะเลือก **ไม่ปรับ Outliers** โดยอัตโนมัติในขั้นตอนนี้ เพื่อรักษาความถูกต้องของข้อมูลตามบริบททางธุรกิจ อย่างไรก็ตาม ในสถานการณ์จริง การจัดการ Outlier ต้องพิจารณาจากบริบทและเป้าหมายการวิเคราะห์อย่างรอบคอบ.

            """)

        else:

            st.info("ไม่พบคอลัมน์ตัวเลขสำหรับวิเคราะห์ Outliers")

        return data
 
    st.sidebar.markdown("## 🛠️ เลือกขั้นตอนทำความสะอาดข้อมูล")

    do_explore = st.sidebar.checkbox("1. Data Exploration", value=True)

    do_duplicates = st.sidebar.checkbox("2. Handle Duplicate Data", value=True)

    do_inconsistent = st.sidebar.checkbox("3. Handle Inconsistent Data", value=True)

    do_missing = st.sidebar.checkbox("4. Handle Missing Data", value=True)

    do_noisy = st.sidebar.checkbox("5. Handle Noisy Data", value=True)

    do_outlier = st.sidebar.checkbox("6. Outlier Detection", value=True)
 
    st.markdown("<hr/>", unsafe_allow_html=True)
 
    if st.button("🚀 เริ่มทำความสะอาดข้อมูล!"):

        st.markdown("## กำลังดำเนินการ Data Cleaning...")

        progress_bar = st.progress(0)

        step_count = 0

        total_steps = sum([do_explore, do_duplicates, do_inconsistent, do_missing, do_noisy, do_outlier])
 
        if do_explore:

            step_count += 1

            st.write(f"**{step_count}/{total_steps}** กำลังทำ: Data Exploration...")

            df = perform_data_exploration(df)

            progress_bar.progress(step_count / total_steps)
 
        if do_duplicates:

            step_count += 1

            st.write(f"**{step_count}/{total_steps}** กำลังทำ: Handle Duplicate Data...")

            df = handle_duplicate_data(df)

            progress_bar.progress(step_count / total_steps)
 
        if do_inconsistent:

            step_count += 1

            st.write(f"**{step_count}/{total_steps}** กำลังทำ: Handle Inconsistent Data...")

            df = handle_inconsistent_data(df)

            progress_bar.progress(step_count / total_steps)
 
        if do_missing:

            step_count += 1

            st.write(f"**{step_count}/{total_steps}** กำลังทำ: Handle Missing Data...")

            df = handle_missing_data(df)

            progress_bar.progress(step_count / total_steps)
 
        if do_noisy:

            step_count += 1

            st.write(f"**{step_count}/{total_steps}** กำลังทำ: Handle Noisy Data...")

            df = handle_noisy_data(df)

            progress_bar.progress(step_count / total_steps)
 
        if do_outlier:

            step_count += 1

            st.write(f"**{step_count}/{total_steps}** กำลังทำ: Outlier Detection & Treatment...")

            df = perform_outlier_analysis(df)

            progress_bar.progress(step_count / total_steps)
 
        st.balloons()

        st.markdown("### ✅ **กระบวนการทำความสะอาดข้อมูลเสร็จสมบูรณ์!**")

        st.markdown("<hr/>", unsafe_allow_html=True)
 
        st.subheader("📊 7. Cleaned Data Summary")

        st.write(f"#### **ก่อนทำความสะอาด:** {df_raw.shape[0]:,} แถว, {df_raw.shape[1]} คอลัมน์")

        st.write(f"#### **หลังทำความสะอาด:** {df.shape[0]:,} แถว, {df.shape[1]} คอลัมน์")
 
        st.markdown("### Cleaned Data Preview (5 แถวแรก)")

        st.dataframe(df.head())
 
        # --- Download Cleaned Data ---

        csv_buffer = df.to_csv(index=False).encode('utf-8')

        st.download_button(

            label="⬇️ ดาวน์โหลด Cleaned Data (.csv)",

            data=csv_buffer,

            file_name="redbull_clean.csv",

            mime="text/csv",

            help="คลิกเพื่อดาวน์โหลดชุดข้อมูลที่ผ่านการทำความสะอาดแล้ว"

        )

else:

    st.info("โปรดอัปโหลดไฟล์ CSV ของคุณเพื่อเริ่มต้นการทำความสะอาดข้อมูลด้านบน 👆")
 
# Placeholder for the return to home button if multiple pages were implemented.

# For a single-page app, this might not be needed or would link elsewhere.

# if st.button("🏠 กลับหน้าหลัก"): # This button might not work as expected in a single-file app

#     st.write("ฟังก์ชัน 'กลับหน้าหลัก' ต้องการการตั้งค่า Streamlit multi-page หรือลิงก์ไปยัง URL อื่น")
 
