# smart_dashboard.py

import streamlit as st
from streamlit_option_menu import option_menu

# ✅ Inject Background Color CSS (works across all pages)
st.markdown("""
    <style>
    .stApp {
        background-color: Violet!important;
    }
    </style>
""", unsafe_allow_html=True)


# Page settings
st.set_page_config(page_title="Smart City Assistant", layout="wide")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Smart City Assistant",
        ["Dashboard Summary", "Citizen Feedback", "Eco Tips", "KPI Forecasting", "Anomaly Detection", "Sustainability Report", "Policy Summarizer", "Chat Assistant"],
        icons=["clipboard-data", "chat-left-text", "tree-fill", "graph-up", "exclamation-triangle", "bar-chart", "file-earmark-text", "chat-dots"],
        menu_icon="house",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "LightBlue"},
            "icon": {"color": "black", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
            "nav-link-selected": {"background-color": "#e74c3c","color": "white"},
        }
    )

# Routing to modules
if selected == "Dashboard Summary":
    from modules import dashboard
    dashboard.run()

elif selected == "Citizen Feedback":
    from modules import feedback
    feedback.run()

elif selected == "Eco Tips":
    from modules import eco_tips
    eco_tips.run()

elif selected == "KPI Forecasting":
    from modules import kpi_forecasting
    kpi_forecasting.run()

elif selected == "Anomaly Detection":
    from modules import anomaly_detection
    anomaly_detection.run()

elif selected == "Sustainability Report":
    from modules import sustainability_report
    sustainability_report.run()

elif selected == "Policy Summarizer":
    from modules import policy_summarizer
    policy_summarizer.run()

elif selected == "Chat Assistant":
    from modules import chat
    chat.run()
