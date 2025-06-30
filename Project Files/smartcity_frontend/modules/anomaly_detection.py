# smartcity_frontend/modules/anomaly_detection.py

import streamlit as st
import requests

def run():
    st.title("⚠️ Anomaly Detection")

    if st.button("Detect Anomalies"):
        with st.spinner("Analyzing..."):
            try:
                response = requests.get("http://127.0.0.1:8000/api/anomaly-detect")
                data = response.json()

                if "anomalies" in data and data["anomalies"]:
                    st.success("✅ Anomalies Detected")
                    for entry in data["anomalies"]:
                        st.markdown(f"""
                        🔺 **Metric**: {entry['metric']}  
                        📍 **Index**: {entry['index']}  
                        📊 **Value**: {entry['value']}
                        """)
                else:
                    st.info("🎉 No anomalies detected!")
            except Exception as e:
                st.error(f"❌ Failed to fetch anomalies: {e}")
