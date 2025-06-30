# app/services/chat_assistant.py
from app.services.granite_llm import ask_granite

def ask_city_assistant(prompt: str) -> str:
    # Just give an instruction-style prompt, because we use an instruct model
    formatted_prompt = (
        "You are an assistant that answers smart city questions about sustainability, green infrastructure, and pollution reduction.\n\n"
        f"Question: {prompt}\nAnswer:"
    )
    return ask_granite(formatted_prompt)
