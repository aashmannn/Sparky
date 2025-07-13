from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
import json

from app.core.database import get_db
from app.services.forecast_service import ForecastService
from app.schemas.forecast import ForecastRequest, ForecastResponse

router = APIRouter()

@router.post("/", response_model=ForecastResponse)
async def generate_forecast(
    forecast_request: ForecastRequest,
    db: Session = Depends(get_db)
):
    """Generate emissions forecast for specified parameters"""
    try:
        forecast_service = ForecastService(db)
        forecast = await forecast_service.generate_forecast(
            supplier_id=forecast_request.supplier_id,
            product_id=forecast_request.product_id,
            forecast_horizon_days=forecast_request.forecast_horizon_days,
            confidence_level=forecast_request.confidence_level
        )
        return forecast
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Forecast generation failed: {str(e)}")

@router.get("/supplier/{supplier_id}")
async def get_supplier_forecast(
    supplier_id: str,
    horizon_days: int = Query(90, ge=1, le=365),
    db: Session = Depends(get_db)
):
    """Get forecast for a specific supplier"""
    try:
        forecast_service = ForecastService(db)
        forecast = await forecast_service.generate_forecast(
            supplier_id=supplier_id,
            forecast_horizon_days=horizon_days
        )
        return forecast
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Forecast generation failed: {str(e)}")

@router.get("/trends")
async def get_forecast_trends(
    db: Session = Depends(get_db)
):
    """Get overall forecast trends and insights"""
    try:
        forecast_service = ForecastService(db)
        trends = await forecast_service.get_forecast_trends()
        return trends
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Trend analysis failed: {str(e)}")

@router.post("/train")
async def retrain_models(
    db: Session = Depends(get_db)
):
    """Retrain the forecasting models with latest data"""
    try:
        forecast_service = ForecastService(db)
        result = await forecast_service.retrain_models()
        return {"message": "Models retrained successfully", "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model retraining failed: {str(e)}")

@router.get("/accuracy")
async def get_model_accuracy(
    db: Session = Depends(get_db)
):
    """Get model accuracy metrics"""
    try:
        forecast_service = ForecastService(db)
        accuracy = await forecast_service.get_model_accuracy()
        return accuracy
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Accuracy calculation failed: {str(e)}") 