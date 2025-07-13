from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.sql import func
from app.core.database import Base

class Incentive(Base):
    __tablename__ = "incentives"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    emission_reduction_threshold = Column(Float)
    financial_incentive = Column(Float)
    eligibility_criteria = Column(Text)  # JSON string
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 