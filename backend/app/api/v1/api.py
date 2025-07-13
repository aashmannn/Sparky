from fastapi import APIRouter
from app.api.v1.endpoints import carbon_events, forecasts, incentives, reports, upload

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(carbon_events.router, prefix="/carbon-events", tags=["carbon-events"])
api_router.include_router(forecasts.router, prefix="/forecast", tags=["forecasts"])
api_router.include_router(incentives.router, prefix="/incentives", tags=["incentives"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
api_router.include_router(upload.router, prefix="/upload", tags=["upload"]) 