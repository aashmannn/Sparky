from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class IncentiveBase(BaseModel):
    name: str
    description: str
    category: str
    type: str
    value: float
    max_value: Optional[float] = None
    is_active: bool = True

class IncentiveCreate(IncentiveBase):
    pass

class IncentiveUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    type: Optional[str] = None
    value: Optional[float] = None
    max_value: Optional[float] = None
    is_active: Optional[bool] = None

class Incentive(IncentiveBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class IncentiveMatch(BaseModel):
    incentive_id: int
    incentive_name: str
    match_score: float
    potential_savings: float
    requirements: List[str]

class IncentiveOpportunity(BaseModel):
    carbon_event_id: int
    matched_incentives: List[IncentiveMatch]
    total_potential_savings: float
    recommended_actions: List[str]
