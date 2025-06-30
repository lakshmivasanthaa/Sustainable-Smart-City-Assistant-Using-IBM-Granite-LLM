from fastapi import APIRouter, HTTPException
from app.services.kpi_file_forecaster import forecast_kpi_from_file
import os

router = APIRouter()

@router.get("/forecast-kpi", tags=["KPI Dashboard"])
def forecast_kpi():
    file_path = "app/data/uploaded_kpi.csv"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="KPI file not found")

    forecast = forecast_kpi_from_file(file_path)
    return forecast
