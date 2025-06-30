from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io
import os

router = APIRouter()

@router.post("/upload-kpi", tags=["KPI Upload"])
async def upload_kpi(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
        df.to_csv("app/data/uploaded_kpi.csv", index=False)
        return {"message": "KPI data uploaded successfully", "rows": len(df)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
