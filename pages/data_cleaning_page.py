import streamlit as st # ไลบรารีสำหรับสร้าง Web Application
import pandas as pd # ไลบรารีสำหรับจัดการข้อมูลในรูปแบบ DataFrame
import numpy as np # ไลบรารีสำหรับคำนวณทางคณิตศาสตร์
import matplotlib.pyplot as plt # ไลบรารีสำหรับสร้างกราฟ
import seaborn as sns # ไลบรารีสำหรับสร้างกราฟที่สวยงามขึ้น
from scipy.stats.mstats import winsorize # ฟังก์ชันสำหรับจัดการ Outlier (Winsorization)
import io # ไลบรารีสำหรับจัดการ Input/Output
import warnings # ไลบรารีสำหรับจัดการคำเตือน
warnings.filterwarnings('ignore') # ไม่แสดงคำเตือน

# ตั้งค่า Streamlit page
st.set_page_config(layout="wide", page_title="Red Bull Data Cleaning App")

# --- Streamlit App Title ---
st.title("🐂 Red Bull Data Cleaning Web Application") # ตั้งชื่อแอปพลิเคชัน
st.markdown("ยินดีต้อนรับสู่แอปพลิเคชัน Data Cleaning ที่จะช่วยคุณทำความสะอาดข้อมูล Red Bull!") # ข้อความต้อนรับ
st.markdown("### ⬆️ อัปโหลดไฟล์ `redbull_workshop_dirty.csv` เพื่อเริ่มต้น") # คำแนะนำเบื้องต้น
st.info("⚠️ แอปพลิเคชันนี้ออกแบบมาสำหรับชุดข้อมูลที่มีโครงสร้างเหมือน `redbull_workshop_dirty.csv` เท่านั้น")

# --- File Uploader ---
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None: # ถ้ามีการอัปโหลดไฟล์แล้ว
    df_raw = pd.read_csv(uploaded_file) # อ่านไฟล์ CSV ที่อัปโหลด
    df = df_raw.copy() # สร้างสำเนาข้อมูลเพื่อไม่ให้แก้ไขข้อมูลต้นฉบับ
    st.success("✅ File uploaded successfully! Ready to clean your data.") # แสดงข้อความแจ้งว่าอัปโหลดสำเร็จ
    
    with st.expander("ดูข้อมูลดิบ (Raw Data Preview)"): # ใช้ expander เพื่อซ่อนข้อมูลดิบ
        st.write("### Raw Data (First 5 Rows)") # หัวข้อแสดงข้อมูลดิบ
        st.dataframe(df_raw.head())

    # --- Data Cleaning Steps (as functions) ---

    def perform_data_exploration(data):
        st.subheader("📊 1. Data Exploration")
        with st.expander("คลิกเพื่อดูรายละเอียด Data Exploration"): # ใช้ expander
            st.write("#### Data Shape:")
            st.write(f"Rows: {data.shape[0]:,}, Columns: {data.shape[1]}")
            st.write("#### Data Info:")
            buffer = io.StringIO()
            data.info(buf=buffer)
            st.text(buffer.getvalue())
            st.write("#### Descriptive Statistics:")
            st.dataframe(data.describe(include='all'))
        return data

    def handle_duplicate_data(data):
        st.subheader("👥 2. Handle Duplicate Data")
        exact_dups = data.duplicated()
        exact_dup_count = exact_dups.sum()
        if exact_dup_count > 0:
            st.warning(f"⚠️ พบข้อมูลซ้ำ 100% จำนวน {exact_dup_count:,} แถว")
            with st.expander("คลิกเพื่อดูตัวอย่างข้อมูลซ้ำ"): # ใช้ expander
                st.dataframe(data[exact_dups])
            data = data.drop_duplicates()
            st.success(f"✅ ลบข้อมูลซ้ำแล้ว: เหลือ {len(data):,} แถว")
        else:
            st.info("ℹ️ ไม่พบ Exact Duplicate ในข้อมูลนี้")
        return data

    def handle_inconsistent_data(data):
        st.subheader("🔄 3. Handle Inconsistent Data")
        cat_cols = ['Region', 'Product_Variant', 'Channel']
        
        with st.expander("คลิกเพื่อดู Unique Values ก่อนแก้ไข"): # ใช้ expander
            st.write("##### Unique Values ก่อนแก้ไข Inconsistent Values:") # หัวข้อย่อยแสดงค่าก่อนแก้ไข
            for col in cat_cols: # วนลูปในแต่ละคอลัมน์
                unique_vals = data[col].unique()
                st.write(f"**📌 {col} ({len(unique_vals)} ค่า):**")
                st.write(unique_vals)

        st.write("##### กำลังแก้ไข Inconsistent Values...")

        # 1. Standardize Region Column
        data['Region'] = data['Region'].str.strip().str.lower()
        region_mapping = {
            'th-central': 'TH-CENTRAL', 'th central': 'TH-CENTRAL',
            'thailand central': 'TH-CENTRAL', 'thailand-central': 'TH-CENTRAL',
            'thailand': 'TH-CENTRAL',
            'usa-east': 'USA-EAST', 'us east': 'USA-EAST',
            'united states east': 'USA-EAST', 'u.s.a.': 'USA-EAST',
            'europe-eu': 'EUROPE-EU', 'eu': 'EUROPE-EU',
            'europe': 'EUROPE-EU', 'european union': 'EUROPE-EU',
            'asia-pacific': 'ASIA-PACIFIC', 'asia-pac': 'ASIA-PACIFIC',
            'apac': 'ASIA-PACIFIC', 'asia pacific': 'ASIA-PACIFIC'
        }
        data['Region'] = data['Region'].replace(region_mapping)
        data['Region'] = data['Region'].str.upper() # แปลงเป็นตัวพิมพ์ใหญ่ทั้งหมด

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
        # Ensure consistent title case for Product_Variant
        data['Product_Variant'] = data['Product_Variant'].apply(lambda x: x.title() if isinstance(x, str) else x)

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
        # Ensure consistent casing for any remaining channels not in mapping or to standardize from `Social Media` to `Social Media`.
        data['Channel'] = data['Channel'].apply(lambda x: x.title() if isinstance(x, str) else x)

        # Convert Date to datetime
        data['Date'] = pd.to_datetime(data['Date'], format='mixed')

        st.success("✅ แก้ไข Inconsistent Values สำเร็จแล้ว!")
        with st.expander("คลิกเพื่อดู Unique Values หลังแก้ไข"): # ใช้ expander
            st.write("##### Unique Values หลังแก้ไข Inconsistent Values:") # หัวข้อย่อยแสดงค่าหลังแก้ไข
            for col in cat_cols:
                unique_vals = data[col].unique()
                st.write(f"**📌 {col} ({len(unique_vals)} ค่า):**")
                st.write(unique_vals)
        return data

    def handle_missing_data(data):
        st.subheader("📭 4. Handle Missing Data")
        missing_count = data.isnull().sum()
        
        if missing_count.sum() > 0: # ถ้ามีค่า Missing
            st.write("##### Missing Values ก่อนแก้ไข:")
            st.dataframe(missing_count[missing_count > 0])

            median_marketing = data['Marketing_Spend'].median()
            data['Marketing_Spend'] = data['Marketing_Spend'].fillna(median_marketing)
            st.info(f'✅ Marketing_Spend: เติมด้วย Median = {median_marketing:,.2f}')

            median_score = data['Customer_Score'].median()
            data['Customer_Score'] = data['Customer_Score'].fillna(median_score)
            st.info(f'✅ Customer_Score: เติมด้วย Median = {median_score}')

            st.success("✅ แก้ไข Missing Values สำเร็จแล้ว!")
            st.write("##### Missing Values หลังแก้ไข:")
            st.write(f"รวม {data.isnull().sum().sum()} ค่า (ควรเป็น 0)")
        else:
            st.info("ℹ️ ไม่พบ Missing Data ในข้อมูลนี้")
        return data

    def handle_noisy_data(data):
        st.subheader("📢 5. Handle Noisy Data")
        st.write("##### ตรวจสอบ Business Logic ก่อนแก้ไข:")
        neg_price = data[data['Unit_Price'] <= 0]
        neg_units = data[data['Units_Sold'] <= 0]
        neg_mkt = data[data['Marketing_Spend'] < 0]
        bad_score = data[(data['Customer_Score'] < 1) | (data['Customer_Score'] > 10)]

        found_noisy = False
        if len(neg_price) > 0:
            st.warning(f"❌ Unit_Price ≤ 0  : {len(neg_price):,} แถว (ราคาต้องเป็นบวก!)")
            found_noisy = True
        if len(neg_units) > 0:
            st.warning(f"❌ Units_Sold ≤ 0  : {len(neg_units):,} แถว (ขายไม่ได้ติดลบ!)")
            found_noisy = True
        if len(neg_mkt) > 0:
            st.warning(f"❌ Marketing < 0   : {len(neg_mkt):,} แถว (งบต้องไม่ติดลบ!)")
            found_noisy = True
        if len(bad_score) > 0:
            st.warning(f"❌ Customer_Score ไม่ใช่ 1-10: {len(bad_score):,} แถว (คะแนนต้องอยู่ระหว่าง 1-10!)")
            found_noisy = True

        if found_noisy:
            initial_rows = len(data)
            data = data[data['Unit_Price'] > 0]
            data = data[data['Units_Sold'] > 0]
            data = data[data['Marketing_Spend'] >= 0]
            data = data[(data['Customer_Score'] >= 1) & (data['Customer_Score'] <= 10)]
            st.success(f"✅ แก้ไข Noisy Data สำเร็จแล้ว: ลบไป {initial_rows - len(data):,} แถว")
        else:
            st.info("ℹ️ ไม่พบ Noisy Data ที่ขัดแย้งกับ Business Logic")
        return data

    def perform_outlier_analysis(data):
        st.subheader("📐 6. Outlier Detection & Treatment")
        st.markdown("##### ตรวจสอบ Outliers ด้วย Boxplot (แสดงผลสำหรับคอลัมน์เชิงตัวเลข)")

        numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
        if 'Customer_Score' in numeric_cols:
            numeric_cols.remove('Customer_Score') # Removed as it's handled in noisy data and range 1-10

        if numeric_cols:
            with st.expander("คลิกเพื่อดู Boxplots ของคอลัมน์เชิงตัวเลข"): # ใช้ expander
                # Create a grid for boxplots for better visualization
                num_cols_per_row = 2
                num_rows = (len(numeric_cols) + num_cols_per_row - 1) // num_cols_per_row
                
                for i in range(num_rows):
                    cols = st.columns(num_cols_per_row)
                    for j in range(num_cols_per_row):
                        idx = i * num_cols_per_row + j
                        if idx < len(numeric_cols):
                            col = numeric_cols[idx]
                            fig, ax = plt.subplots(figsize=(8, 2))
                            sns.boxplot(x=data[col], ax=ax)
                            ax.set_title(f'Boxplot of {col}')
                            cols[j].pyplot(fig)
                            plt.close(fig)

            st.markdown("""
            **💡 หมายเหตุเกี่ยวกับการจัดการ Outliers:**
            ใน Workshop นี้ เราได้ตัดสินใจ **ไม่ปรับค่า Outliers** ด้วย `winsorize` หรือวิธีการอื่น ๆ ในขั้นตอนนี้
            เนื่องจากเกรงว่าการปรับค่าอาจทำให้ข้อมูลคลาดเคลื่อนจาก Business Logic ที่แท้จริง
            การจัดการ Outlier ควรพิจารณาอย่างรอบคอบตามบริบททางธุรกิจและวัตถุประสงค์ของการวิเคราะห์.
            """)
        else:
            st.info("ℹ️ ไม่พบคอลัมน์ตัวเลขสำหรับวิเคราะห์ Outliers")
        return data

    # --- Sidebar for Step Selection ---
st.sidebar.header("⚙️ เลือกขั้นตอน Data Cleaning")
do_explore = st.sidebar.checkbox("1. Data Exploration", value=True)
do_duplicates = st.sidebar.checkbox("2. Handle Duplicate Data", value=True)
do_inconsistent = st.sidebar.checkbox("3. Handle Inconsistent Data", value=True)
do_missing = st.sidebar.checkbox("4. Handle Missing Data", value=True)
do_noisy = st.sidebar.checkbox("5. Handle Noisy Data", value=True)
do_outlier = st.sidebar.checkbox("6. Outlier Detection", value=True)

st.markdown("---  ") # เส้นแบ่ง

if st.button("🚀 เริ่มต้นทำความสะอาดข้อมูล"): # ปุ่มสำหรับเริ่มกระบวนการ Data Cleaning
    st.write("### กำลังดำเนินการ Data Cleaning...")
    
    with st.spinner('กำลังประมวลผลข้อมูล...'): # Spinner สำหรับแสดงสถานะการโหลด
        # Apply cleaning steps based on user selection
        if do_explore:
            df = perform_data_exploration(df)
        if do_duplicates:
            df = handle_duplicate_data(df)
        if do_inconsistent:
            df = handle_inconsistent_data(df)
        if do_missing:
            df = handle_missing_data(df)
        if do_noisy:
            df = handle_noisy_data(df)
        if do_outlier:
            df = perform_outlier_analysis(df)

    st.markdown("---  ")
    st.subheader("✅ 7. Cleaned Data Summary")
    st.write(f"#### 📥 ข้อมูลเริ่มต้น: {df_raw.shape[0]:,} แถว, {df_raw.shape[1]} คอลัมน์")
    st.write(f"#### 📤 ข้อมูลหลังทำความสะอาด: {df.shape[0]:,} แถว, {df.shape[1]} คอลัมน์")

    st.write("### Cleaned Data (First 5 Rows)")
    st.dataframe(df.head())

    # --- Download Cleaned Data ---
    csv_buffer = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ ดาวน์โหลดข้อมูลที่ทำความสะอาดแล้ว (.csv)",
        data=csv_buffer,
        file_name="redbull_clean.csv",
        mime="text/csv",
        help="คลิกเพื่อดาวน์โหลดชุดข้อมูลที่ผ่านการทำความสะอาดแล้ว"
    )
else:
    st.info("⬆️ กรุณาอัปโหลดไฟล์ CSV เพื่อเริ่มต้นใช้งานแอปพลิเคชัน")

st.markdown("---  ")
# Optional: Link back to a home page if this is a multi-page app
if st.button("🏠 กลับหน้าหลัก (ถ้ามี)"):
    st.switch_page("app.py")
