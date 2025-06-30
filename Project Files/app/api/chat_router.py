# app/api/chat_router.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_assistant import ask_city_assistant

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat/ask")
def chat_with_assistant(req: ChatRequest):
    response = ask_city_assistant(req.prompt)
    return {"response": response}
