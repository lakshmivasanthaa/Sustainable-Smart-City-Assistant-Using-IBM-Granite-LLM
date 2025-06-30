# smartcity_frontend/modules/dashboard.py

import streamlit as st




def run():
    st.title("📊 Smart Dashboard Overview")

    city = st.selectbox("City", ["Pune", "Mumbai", "Delhi"], index=0)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="💧 Water Usage", value="78000")

    with col2:
        st.metric(label="⚡ Energy Consumption", value="10500")

    with col3:
        st.metric(label="🌫️ Air Quality Index", value="40")
