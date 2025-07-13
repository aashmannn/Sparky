from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class CarbonEvent(Base):
    __tablename__ = "carbon_events"
    
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(String(100), index=True, nullable=False)
    product_id = Column(String(100), index=True, nullable=True)
    event_type = Column(String(50), nullable=False)  # 'transport', 'manufacturing', 'energy', etc.
    emissions_kg_co2e = Column(Float, nullable=False)
    activity_data = Column(Text, nullable=True)  # JSON string with activity details
    emission_factor = Column(Float, nullable=True)
    source_document = Column(String(255), nullable=True)  # File path or reference
    verification_status = Column(String(20), default="pending")  # pending, verified, rejected
    audit_trail = Column(Text, nullable=True)  # JSON string with audit information
    blockchain_hash = Column(String(255), nullable=True)
    extracted_data = Column(Text, nullable=True)  # JSON string with extracted data from documents
    confidence_score = Column(Float, nullable=True)  # Confidence score for AI extraction
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    timestamp = Column(DateTime(timezone=True), nullable=False)  # When the emission event occurred
    
    def __repr__(self):
        return f"<CarbonEvent(id={self.id}, supplier_id='{self.supplier_id}', emissions={self.emissions_kg_co2e}kg CO2e)>" 