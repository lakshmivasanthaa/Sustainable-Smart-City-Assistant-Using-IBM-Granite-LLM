import streamlit as st
import requests

def run():
    st.title("🏙️ Sustainability Report Generator")

    st.write("Generate a sustainability report based on your city's KPI data.")

    # Input fields
    city_name = st.text_input("City Name")
    kpi_data = st.text_area("KPI Data (e.g., Water, Energy, AQI)", height=200)

    # Generate Report button
    if st.button("Generate AI Report"):
        if city_name and kpi_data:
            payload = {
                "city_name": city_name,
                "kpi_data": kpi_data
            }

            try:
                response = requests.post("http://127.0.0.1:8000/api/generate-report", json=payload)
                if response.status_code == 200:
                    report = response.json().get("report", "")
                    st.subheader("🌿 Sustainability Report:")
                    st.markdown(report)

                    # Offer download
                    st.download_button(
                        label="📥 Download Report",
                        data=report,
                        file_name=f"{city_name}_sustainability_report.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"Failed to generate report: {response.status_code}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter both City Name and KPI Data.")
