from pydantic import BaseModel
from typing import Optional, Dict, Any

class ParsedData(BaseModel):
    total_amount: Optional[float] = None
    fuel_consumption: Optional[float] = None
    distance_km: Optional[float] = None
    energy_consumption: Optional[float] = None
    waste_generated: Optional[float] = None
    emission_factor: Optional[float] = None
    calculated_emissions: Optional[float] = None

class UploadResponse(BaseModel):
    status: str
    message: Optional[str] = None
    upload_id: Optional[str] = None
    extracted_data: Optional[Dict[str, Any]] = None
    confidence_score: Optional[float] = None
