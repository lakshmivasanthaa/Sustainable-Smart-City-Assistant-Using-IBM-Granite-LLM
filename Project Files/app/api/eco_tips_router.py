from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from app.services.granite_llm import generate_eco_tip

router = APIRouter()

class EcoTipResponse(BaseModel):
    tip: str

@router.get("/get-eco-tips", response_model=EcoTipResponse)
async def get_eco_tip(topic: str = Query(..., description="Enter a sustainability topic like energy, water, waste")):
    try:
        result = generate_eco_tip(topic)
        return {"tip": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
