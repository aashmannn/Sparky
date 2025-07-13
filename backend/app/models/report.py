from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Text
from sqlalchemy.sql import func
from app.core.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    report_type = Column(String(50), nullable=False)
    report_date = Column(Date, nullable=False)
    data_period_start = Column(Date)
    data_period_end = Column(Date)
    total_emissions = Column(Float)
    report_data = Column(Text)  # JSON string
    file_path = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 