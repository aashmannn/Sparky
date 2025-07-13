from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from app.core.database import get_db
from app.models.carbon_event import CarbonEvent
from app.schemas.carbon_event import CarbonEventCreate, CarbonEventResponse, CarbonEventUpdate

router = APIRouter()

@router.get("/", response_model=List[CarbonEventResponse])
async def get_carbon_events(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    supplier_id: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    """Get carbon events with optional filtering"""
    query = db.query(CarbonEvent)
    
    if supplier_id:
        query = query.filter(CarbonEvent.supplier_id == supplier_id)
    
    if start_date:
        query = query.filter(CarbonEvent.timestamp >= start_date)
    
    if end_date:
        query = query.filter(CarbonEvent.timestamp <= end_date)
    
    carbon_events = query.offset(skip).limit(limit).all()
    return carbon_events

@router.post("/", response_model=CarbonEventResponse)
async def create_carbon_event(
    carbon_event: CarbonEventCreate,
    db: Session = Depends(get_db)
):
    """Create a new carbon event"""
    db_carbon_event = CarbonEvent(**carbon_event.dict())
    db.add(db_carbon_event)
    db.commit()
    db.refresh(db_carbon_event)
    return db_carbon_event

@router.get("/{carbon_event_id}", response_model=CarbonEventResponse)
async def get_carbon_event(
    carbon_event_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific carbon event by ID"""
    carbon_event = db.query(CarbonEvent).filter(CarbonEvent.id == carbon_event_id).first()
    if not carbon_event:
        raise HTTPException(status_code=404, detail="Carbon event not found")
    return carbon_event

@router.put("/{carbon_event_id}", response_model=CarbonEventResponse)
async def update_carbon_event(
    carbon_event_id: int,
    carbon_event_update: CarbonEventUpdate,
    db: Session = Depends(get_db)
):
    """Update a carbon event"""
    db_carbon_event = db.query(CarbonEvent).filter(CarbonEvent.id == carbon_event_id).first()
    if not db_carbon_event:
        raise HTTPException(status_code=404, detail="Carbon event not found")
    
    for field, value in carbon_event_update.dict(exclude_unset=True).items():
        setattr(db_carbon_event, field, value)
    
    db.commit()
    db.refresh(db_carbon_event)
    return db_carbon_event

@router.delete("/{carbon_event_id}")
async def delete_carbon_event(
    carbon_event_id: int,
    db: Session = Depends(get_db)
):
    """Delete a carbon event"""
    carbon_event = db.query(CarbonEvent).filter(CarbonEvent.id == carbon_event_id).first()
    if not carbon_event:
        raise HTTPException(status_code=404, detail="Carbon event not found")
    
    db.delete(carbon_event)
    db.commit()
    return {"message": "Carbon event deleted successfully"}

@router.get("/summary/dashboard")
async def get_carbon_summary(
    db: Session = Depends(get_db)
):
    """Get carbon emissions summary for dashboard"""
    # Get total emissions for current month
    current_month_start = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    total_emissions = db.query(CarbonEvent).filter(
        CarbonEvent.timestamp >= current_month_start
    ).with_entities(
        db.func.sum(CarbonEvent.emissions_kg_co2e).label("total_emissions")
    ).scalar() or 0
    
    # Get top suppliers by emissions
    top_suppliers = db.query(CarbonEvent).filter(
        CarbonEvent.timestamp >= current_month_start
    ).with_entities(
        CarbonEvent.supplier_id,
        db.func.sum(CarbonEvent.emissions_kg_co2e).label("total_emissions")
    ).group_by(CarbonEvent.supplier_id).order_by(
        db.func.sum(CarbonEvent.emissions_kg_co2e).desc()
    ).limit(5).all()
    
    return {
        "total_emissions_kg_co2e": float(total_emissions),
        "top_suppliers": [
            {"supplier_id": supplier.supplier_id, "emissions": float(supplier.total_emissions)}
            for supplier in top_suppliers
        ]
    } 