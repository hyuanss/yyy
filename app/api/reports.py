"""
File: app/api/reports.py
Purpose: Report endpoints for learning summaries.
Key functions/classes: learning_report().
Usage: POST /api/reports/learning.
"""
from fastapi import APIRouter, Depends, HTTPException

from app.core.auth import verify_api_key
from app.db.repository import save_report_log
from app.db.session import SessionLocal
from app.schemas.report import LearningReportRequest, LearningReportResponse
from app.services.report_service import ReportService

router = APIRouter(tags=["reports"], dependencies=[Depends(verify_api_key)])
report_service = ReportService()


@router.post("/reports/learning", response_model=LearningReportResponse)
def learning_report(payload: LearningReportRequest) -> LearningReportResponse:
    """Generate a learning report from key points and weaknesses."""
    try:
        report = report_service.generate_learning_report(payload)
        if SessionLocal:
            with SessionLocal() as db:
                save_report_log(
                    db,
                    student_name=payload.student_name,
                    key_points=payload.key_points,
                    weak_points=payload.weak_points,
                    suggestions=payload.suggestions,
                    report=report,
                )
        return LearningReportResponse(report=report)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"learning_report failed: {exc}") from exc
