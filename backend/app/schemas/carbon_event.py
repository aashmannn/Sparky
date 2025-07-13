from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class CarbonEventBase(BaseModel):
    supplier_id: str = Field(..., description="Supplier identifier")
    product_id: Optional[str] = Field(None, description="Product identifier")
    event_type: str = Field(..., description="Type of emission event")
    emissions_kg_co2e: float = Field(..., gt=0, description="Emissions in kg CO2e")
    activity_data: Optional[Dict[str, Any]] = Field(None, description="Activity details")
    emission_factor: Optional[float] = Field(None, description="Emission factor used")
    source_document: Optional[str] = Field(None, description="Source document reference")
    timestamp: datetime = Field(..., description="When the emission event occurred")

class CarbonEventCreate(CarbonEventBase):
    pass

class CarbonEventUpdate(BaseModel):
    supplier_id: Optional[str] = None
    product_id: Optional[str] = None
    event_type: Optional[str] = None
    emissions_kg_co2e: Optional[float] = Field(None, gt=0)
    activity_data: Optional[Dict[str, Any]] = None
    emission_factor: Optional[float] = None
    source_document: Optional[str] = None
    verification_status: Optional[str] = None
    audit_trail: Optional[Dict[str, Any]] = None
    blockchain_hash: Optional[str] = None
    timestamp: Optional[datetime] = None

class CarbonEventResponse(CarbonEventBase):
    id: int
    verification_status: str
    audit_trail: Optional[Dict[str, Any]] = None
    blockchain_hash: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True 