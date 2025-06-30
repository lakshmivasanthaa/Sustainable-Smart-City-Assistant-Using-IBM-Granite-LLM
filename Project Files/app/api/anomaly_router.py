# app/api/anomaly_router.py

from fastapi import APIRouter, HTTPException
import os
from app.services.anomaly_file_checker import detect_anomalies

router = APIRouter()

@router.get("/anomaly-detect", tags=["Anomaly Detection"])
async def anomaly_detect():
    file_path = "app/data/uploaded_kpi.csv"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="No uploaded KPI file found.")

    result = detect_anomalies(file_path)
    return result
