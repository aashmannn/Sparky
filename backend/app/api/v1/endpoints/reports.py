from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
import io

from app.core.database import get_db
from app.services.report_service import ReportService
from app.schemas.report import ReportRequest, ReportResponse

router = APIRouter()

@router.post("/generate", response_model=ReportResponse)
async def generate_esg_report(
    report_request: ReportRequest,
    db: Session = Depends(get_db)
):
    """Generate a comprehensive ESG report"""
    try:
        report_service = ReportService(db)
        report = await report_service.generate_esg_report(
            report_type=report_request.report_type,
            start_date=report_request.start_date,
            end_date=report_request.end_date,
            suppliers=report_request.suppliers,
            include_forecasts=report_request.include_forecasts,
            include_incentives=report_request.include_incentives
        )
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report generation failed: {str(e)}")

@router.get("/download/{report_id}")
async def download_report(
    report_id: str,
    format: str = "pdf",
    db: Session = Depends(get_db)
):
    """Download a generated report in specified format"""
    try:
        report_service = ReportService(db)
        report_data = await report_service.download_report(report_id, format)
        
        if format.lower() == "pdf":
            return Response(
                content=report_data,
                media_type="application/pdf",
                headers={"Content-Disposition": f"attachment; filename=esg_report_{report_id}.pdf"}
            )
        elif format.lower() == "csv":
            return Response(
                content=report_data,
                media_type="text/csv",
                headers={"Content-Disposition": f"attachment; filename=esg_report_{report_id}.csv"}
            )
        else:
            raise HTTPException(status_code=400, detail="Unsupported format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report download failed: {str(e)}")

@router.get("/templates")
async def get_report_templates(
    db: Session = Depends(get_db)
):
    """Get available report templates"""
    try:
        report_service = ReportService(db)
        templates = await report_service.get_report_templates()
        return templates
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch templates: {str(e)}")

@router.get("/compliance/check")
async def check_compliance_status(
    db: Session = Depends(get_db)
):
    """Check compliance status against SEC and EU requirements"""
    try:
        report_service = ReportService(db)
        compliance = await report_service.check_compliance_status()
        return compliance
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Compliance check failed: {str(e)}")

@router.get("/history")
async def get_report_history(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get history of generated reports"""
    try:
        report_service = ReportService(db)
        history = await report_service.get_report_history(skip, limit)
        return history
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch report history: {str(e)}") 