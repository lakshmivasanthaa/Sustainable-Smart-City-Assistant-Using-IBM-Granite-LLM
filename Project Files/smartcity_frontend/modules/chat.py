import streamlit as st
import requests

# Backend FastAPI endpoint for chat
API_URL = "http://127.0.0.1:8000/chat/ask"

def run():
    st.title("💬 Chat with Smart City Assistant")
    st.markdown("Ask anything about sustainability, smart policies, or smart city planning!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Type your question here", key="chat_input")

    if st.button("Send"):
        if user_input.strip():
            with st.spinner("Thinking..."):
                try:
                    response = requests.post(API_URL, json={"prompt": user_input})
                    if response.status_code == 200:
                        assistant_reply = response.json().get("response", "No reply generated.")
                        st.session_state.chat_history.append(("You", user_input))
                        st.session_state.chat_history.append(("Assistant", assistant_reply))
                    else:
                        st.error(f"API Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Error connecting to Chat API: {e}")

    # Display chat history
    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 Assistant:** {msg}")
