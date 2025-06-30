# app/api/policy_router.py

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.policy_summarizer import summarize_policy

router = APIRouter()

@router.post("/summarize-policy", tags=["Policy Summarizer"])
async def summarize(file: UploadFile = File(None), text: str = Form(None)):
    try:
        if file:
            content = await file.read()
            text = content.decode("utf-8")

        if not text:
            raise HTTPException(status_code=400, detail="No policy text provided.")

        summary = summarize_policy(text)
        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
