# smartcity_frontend/modules/policy_summarizer.py

import streamlit as st
import requests

def run():
    st.title("📄 Policy Summarizer")
    st.write("Upload a smart city policy file or paste text below to get a summary.")

    uploaded_file = st.file_uploader("Upload Policy (.txt)", type="txt")
    text_input = st.text_area("Or Enter Policy Text")

    if st.button("Summarize Policy"):
        with st.spinner("Generating summary..."):
            files = {"file": uploaded_file} if uploaded_file else None
            data = {"text": text_input}

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/summarize-policy",
                    files=files,
                    data=data
                )
                result = response.json()
                if "summary" in result:
                    st.subheader("📝 Summary:")
                    st.success(result["summary"])
                else:
                    st.error("Failed to generate summary.")
            except Exception as e:
                st.error(f"Error: {e}")
