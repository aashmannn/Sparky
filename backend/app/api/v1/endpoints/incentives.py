from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.core.database import get_db
from app.services.incentive_service import IncentiveService
from app.schemas.incentive import IncentiveMatch, IncentiveOpportunity

router = APIRouter()

@router.get("/", response_model=List[IncentiveOpportunity])
async def get_available_incentives(
    db: Session = Depends(get_db)
):
    """Get all available sustainability incentives"""
    try:
        incentive_service = IncentiveService(db)
        incentives = await incentive_service.get_available_incentives()
        return incentives
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch incentives: {str(e)}")

@router.post("/match", response_model=List[IncentiveMatch])
async def match_emissions_to_incentives(
    supplier_id: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Match emissions reductions to available incentives"""
    try:
        incentive_service = IncentiveService(db)
        matches = await incentive_service.match_emissions_to_incentives(supplier_id)
        return matches
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Incentive matching failed: {str(e)}")

@router.get("/opportunities")
async def get_incentive_opportunities(
    db: Session = Depends(get_db)
):
    """Get current incentive opportunities for the organization"""
    try:
        incentive_service = IncentiveService(db)
        opportunities = await incentive_service.get_incentive_opportunities()
        return opportunities
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch opportunities: {str(e)}")

@router.get("/financial-impact")
async def get_financial_impact(
    db: Session = Depends(get_db)
):
    """Calculate total financial impact of available incentives"""
    try:
        incentive_service = IncentiveService(db)
        impact = await incentive_service.calculate_financial_impact()
        return impact
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Financial impact calculation failed: {str(e)}")

@router.post("/apply/{incentive_id}")
async def apply_for_incentive(
    incentive_id: str,
    db: Session = Depends(get_db)
):
    """Apply for a specific incentive"""
    try:
        incentive_service = IncentiveService(db)
        result = await incentive_service.apply_for_incentive(incentive_id)
        return {"message": "Incentive application submitted successfully", "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Incentive application failed: {str(e)}") 