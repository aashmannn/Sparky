from pydantic import BaseModel
from typing import Optional, List

class ReportRequest(BaseModel):
    report_type: str
    filters: Optional[dict] = None

class ReportResponse(BaseModel):
    report_type: str
    data: List[dict]
    generated_at: str
