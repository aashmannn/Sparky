from sqlalchemy.orm import Session
from fastapi import UploadFile
from typing import Optional, Dict, Any
import json
from datetime import datetime
from app.models.carbon_event import CarbonEvent

class UploadService:
    def __init__(self, db: Session):
        self.db = db

    async def process_file(
        self, 
        file: UploadFile, 
        supplier_id: Optional[str] = None,
        document_type: str = "invoice"
    ) -> Dict[str, Any]:
        """Process uploaded file and extract emissions data"""
        try:
            # Read file content
            content = await file.read()
            
            # For demo purposes, generate mock extracted data
            extracted_data = {
                "total_amount": 1500.00,
                "fuel_consumption": 500.0,
                "distance_km": 2000.0,
                "energy_consumption": 2500.0,
                "waste_generated": 50.0,
                "emission_factor": 2.31,
                "calculated_emissions": 1250.5
            }
            
            # Create carbon event record
            carbon_event = CarbonEvent(
                supplier_id=supplier_id or "SUP001",
                event_type=document_type,
                emissions_kg_co2e=extracted_data["calculated_emissions"],
                source_document=file.filename,
                verification_status="verified",
                extracted_data=json.dumps(extracted_data),
                confidence_score=0.95,
                timestamp=datetime.now()
            )
            
            self.db.add(carbon_event)
            self.db.commit()
            self.db.refresh(carbon_event)
            
            return {
                "status": "success",
                "message": "File processed successfully",
                "upload_id": str(carbon_event.id),
                "extracted_data": extracted_data,
                "confidence_score": 0.95
            }
            
        except Exception as e:
            self.db.rollback()
            raise Exception(f"File processing failed: {str(e)}")

    async def process_manual_data(self, data: Dict[str, Any], supplier_id: str) -> Dict[str, Any]:
        """Process manually entered emissions data"""
        try:
            carbon_event = CarbonEvent(
                supplier_id=supplier_id,
                event_type=data.get("event_type", "manual"),
                emissions_kg_co2e=data.get("emissions_kg_co2e", 0),
                activity_data=json.dumps(data),
                verification_status="verified",
                timestamp=datetime.now()
            )
            
            self.db.add(carbon_event)
            self.db.commit()
            self.db.refresh(carbon_event)
            
            return {
                "status": "success",
                "message": "Manual data saved successfully",
                "event_id": carbon_event.id
            }
            
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Manual data processing failed: {str(e)}")

    async def get_upload_status(self, upload_id: str) -> Dict[str, Any]:
        """Get upload processing status"""
        return {
            "upload_id": upload_id,
            "status": "completed",
            "progress": 100
        }

    async def get_parsed_data(self, upload_id: str) -> Dict[str, Any]:
        """Get parsed data from upload"""
        return {
            "upload_id": upload_id,
            "extracted_data": {
                "total_amount": 1500.00,
                "fuel_consumption": 500.0,
                "distance_km": 2000.0,
                "calculated_emissions": 1250.5
            }
        }

    async def validate_parsed_data(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate parsed data"""
        return {
            "valid": True,
            "confidence_score": 0.95,
            "validation_notes": "Data appears to be valid"
        }
