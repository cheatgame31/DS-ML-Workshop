import streamlit as st
 
st.set_page_config(page_title="MyApp", layout="wide")
 
st.title("🏠 หน้าหลัก ")

st.write("### Boot Camp: Data Science and Machine Learning")

st.info("7 Day Intensive Hands-on Workshop")

st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")
 
if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):

    st.switch_page("pages/app1_discount_calc.py")


elif st.button("💰 Customer Data Cleaner"):

    st.switch_page("pages/clean_customers.py")


elif st.button("💰 My App CLean Data"):

    st.switch_page("pages/test.py")


elif st.button("💰 Clean App"):

    st.switch_page("pages/clean_app.py")


elif st.button("💰 energy_inventory.py"):

    st.switch_page("pages/energy_inventory.py")


elif st.button("💰 energy_inventory.py"):

    st.switch_page("pages/energy_inventory.py")
 
 
