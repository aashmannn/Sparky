from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
import json

from app.core.database import get_db
from app.services.upload_service import UploadService
from app.schemas.upload import UploadResponse, ParsedData

router = APIRouter()

@router.post("/file", response_model=UploadResponse)
async def upload_file(
    file: UploadFile = File(...),
    supplier_id: Optional[str] = Form(None),
    document_type: Optional[str] = Form("invoice"),
    db: Session = Depends(get_db)
):
    """Upload and process a file (PDF, CSV, etc.) for emissions data extraction"""
    try:
        upload_service = UploadService(db)
        
        # Validate file type
        allowed_types = [
            "application/pdf", 
            "text/csv", 
            "text/plain",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ]
        if file.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail=f"Unsupported file type: {file.content_type}")
        
        # Process the file
        result = await upload_service.process_file(
            file=file,
            supplier_id=supplier_id,
            document_type=document_type or "invoice"
        )
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")

@router.post("/bulk")
async def upload_bulk_files(
    files: List[UploadFile] = File(...),
    supplier_id: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    """Upload multiple files for batch processing"""
    try:
        upload_service = UploadService(db)
        results = []
        
        for file in files:
            result = await upload_service.process_file(
                file=file,
                supplier_id=supplier_id
            )
            results.append(result)
        
        return {
            "message": f"Processed {len(results)} files",
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bulk upload failed: {str(e)}")

@router.post("/manual")
async def manual_data_entry(
    data: dict,
    supplier_id: str,
    db: Session = Depends(get_db)
):
    """Manually enter emissions data"""
    try:
        upload_service = UploadService(db)
        result = await upload_service.process_manual_data(data, supplier_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Manual data entry failed: {str(e)}")

@router.get("/status/{upload_id}")
async def get_upload_status(
    upload_id: str,
    db: Session = Depends(get_db)
):
    """Get the status of a file upload/processing job"""
    try:
        upload_service = UploadService(db)
        status = await upload_service.get_upload_status(upload_id)
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get upload status: {str(e)}")

@router.get("/parsed-data/{upload_id}")
async def get_parsed_data(
    upload_id: str,
    db: Session = Depends(get_db)
):
    """Get the parsed data from a processed upload"""
    try:
        upload_service = UploadService(db)
        data = await upload_service.get_parsed_data(upload_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get parsed data: {str(e)}")

@router.post("/validate")
async def validate_parsed_data(
    parsed_data: ParsedData,
    db: Session = Depends(get_db)
):
    """Validate parsed data before saving to database"""
    try:
        upload_service = UploadService(db)
        validation_result = await upload_service.validate_parsed_data(parsed_data.dict())
        return validation_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Data validation failed: {str(e)}") 