from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ForecastDataPoint(BaseModel):
    date: datetime
    predicted_emissions: float = Field(..., ge=0, description="Predicted emissions in kg CO2e")
    confidence_lower: float = Field(..., ge=0, description="Lower confidence bound")
    confidence_upper: float = Field(..., ge=0, description="Upper confidence bound")

class ForecastRequest(BaseModel):
    supplier_id: Optional[str] = Field(None, description="Supplier identifier")
    product_id: Optional[str] = Field(None, description="Product identifier")
    forecast_horizon_days: int = Field(90, ge=1, le=365, description="Forecast horizon in days")
    confidence_level: float = Field(0.95, ge=0.5, le=0.99, description="Confidence level for intervals")

class ForecastResponse(BaseModel):
    supplier_id: Optional[str]
    product_id: Optional[str]
    forecast_horizon_days: int
    confidence_level: float
    forecast_data: List[ForecastDataPoint]
    model_accuracy: float
    generated_at: datetime
    
    class Config:
        from_attributes = True 