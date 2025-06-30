from fastapi import FastAPI
from app.api.chat_router import router as chat_router
from app.api.policy_router import router as policy_router
from app.api.eco_tips_router import router as eco_tips_router
from app.api.report_router import router as report_router
from app.api.feedback_router import router as feedback_router
from app.api.vector_router import router as vector_router
from app.api.kpi_upload_router import router as kpi_upload_router
from app.api.dashboard_router import router as dashboard_router
from app.api.kpi_upload_router import router as kpi_upload_router
from app.api.kpi_forecast_router import router as kpi_forecast_router
from app.api import anomaly_router 
from app.api.report_router import router as report_router
from app.api.policy_router import router as policy_router
from app.api.chat_router import router as chat_router


app = FastAPI()

app.include_router(chat_router,tags=["Chat Assistant"])
app.include_router(policy_router, prefix="/policy", tags=["Policy Summarizer"])
app.include_router(eco_tips_router, tags=["Eco Tips"])
app.include_router(report_router, tags=["Reports"])
app.include_router(feedback_router,tags=["Feedback"])
app.include_router(vector_router, tags=["Vector Search"])
app.include_router(kpi_upload_router)
app.include_router(dashboard_router)
app.include_router(kpi_upload_router, prefix="/api")
app.include_router(kpi_forecast_router, prefix="/api")
app.include_router(anomaly_router.router, prefix="/api")
app.include_router(report_router, prefix="/api") 
app.include_router(policy_router, prefix="/api")
app.include_router(chat_router)
