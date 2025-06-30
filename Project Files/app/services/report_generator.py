# app/services/report_generator.py

from app.services.granite_llm import ask_granite

def generate_sustainability_report(city_name: str, kpi_data: str) -> str:
    try:
        prompt = (
            f"Generate a detailed smart city sustainability report for {city_name}.\n\n"
            f"KPI Data:\n{kpi_data}\n\n"
            "Include water usage, energy consumption, air quality, and future suggestions."
        )
        return ask_granite(prompt)
    except Exception as e:
        return f"Error generating report: {str(e)}"
