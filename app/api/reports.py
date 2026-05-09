"""
File: app/api/reports.py
Purpose: Report endpoints for learning summaries.
Key functions/classes: learning_report().
Usage: POST /api/reports/learning.
"""
from fastapi import APIRouter, HTTPException

from app.schemas.report import LearningReportRequest, LearningReportResponse
from app.services.report_service import ReportService

router = APIRouter(tags=["reports"])
report_service = ReportService()


@router.post("/reports/learning", response_model=LearningReportResponse)
def learning_report(payload: LearningReportRequest) -> LearningReportResponse:
    """Generate a learning report from key points and weaknesses."""
    try:
        report = report_service.generate_learning_report(payload)
        return LearningReportResponse(report=report)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"learning_report failed: {exc}") from exc
