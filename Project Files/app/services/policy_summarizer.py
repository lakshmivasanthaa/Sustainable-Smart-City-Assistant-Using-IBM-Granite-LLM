# app/services/policy_summarizer.py

from app.services.granite_llm import ask_granite

def summarize_policy(text: str) -> str:
    prompt = f"Summarize this smart city policy in simple terms:\n{text}"
    return ask_granite(prompt)
