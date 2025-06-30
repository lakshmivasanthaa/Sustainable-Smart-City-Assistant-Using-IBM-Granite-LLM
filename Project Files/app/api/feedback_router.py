from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.feedback_handler import save_feedback, get_all_feedback

router = APIRouter()

# Request model
class FeedbackRequest(BaseModel):
    user: str
    comment: str

# POST: submit feedback
@router.post("/feedback")
async def submit_feedback(feedback: FeedbackRequest):
    try:
        message = save_feedback(feedback.user, feedback.comment)
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET: retrieve all feedback
@router.get("/feedback")
async def fetch_feedback():
    try:
        return {"feedback": get_all_feedback()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
