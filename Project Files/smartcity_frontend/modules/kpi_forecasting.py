# smartcity_frontend/modules/kpi_forecasting.py

import streamlit as st
import requests
import pandas as pd

def run():
    st.title("📈 KPI Forecasting")

    if st.button("Fetch KPI Forecast"):
        try:
            # Call the backend API that reads uploaded_kpi.csv
            response = requests.get("http://localhost:8000/api/forecast-kpi")

            if response.status_code == 200:
                data = response.json()
                st.success("✅ Forecast Retrieved Successfully")

                # Convert the JSON dict to a DataFrame for display
                df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
                st.dataframe(df)

            else:
                st.error(f"❌ Failed to fetch forecast: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
