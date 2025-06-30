import sys
import os

# ✅ Add root project folder to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import streamlit as st
from app.services.feedback_handler import save_feedback

def run():
    st.title("Citizen Feedback Form")

    st.markdown("Please provide your feedback related to smart city issues.")

    # Input fields
    user = st.text_input("Your Name")
    category = st.selectbox("Category", ["Water", "Energy", "Waste Management", "Public Transport", "Other"])
    message = st.text_area("Your Message")

    if st.button("Submit Feedback"):
        if user and category and message:
            save_feedback(user, category, message)
            st.success("Thank you for your feedback!")
        else:
            st.error("Please fill in all the fields.")
