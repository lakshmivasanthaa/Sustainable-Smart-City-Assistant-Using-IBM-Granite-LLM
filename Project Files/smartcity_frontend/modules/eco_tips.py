# smartcity_frontend/modules/eco_tips.py

import streamlit as st



def run():
    st.title("🌿 Eco Tips")

    keyword = st.text_input("Enter a keyword (e.g., plastic, solar, water):")

    if keyword:
        # Placeholder tip logic
        if "plastic" in keyword.lower():
            st.success("♻️ Tip: Use reusable bags instead of plastic ones!")
        elif "solar" in keyword.lower():
            st.success("☀️ Tip: Install solar panels to reduce grid electricity usage.")
        elif "water" in keyword.lower():
            st.success("🚿 Tip: Fix leaking taps to conserve water.")
        else:
            st.success("✅ Tip: Live sustainably. Every small step matters!")
