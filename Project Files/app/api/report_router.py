# app/api/report_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.report_generator import generate_sustainability_report

router = APIRouter()

class ReportRequest(BaseModel):
    city_name: str
    kpi_data: str

@router.post("/generate-report", tags=["Sustainability Report"])
def generate_report(data: ReportRequest):
    result = generate_sustainability_report(data.city_name, data.kpi_data)
    return {"report": result}
