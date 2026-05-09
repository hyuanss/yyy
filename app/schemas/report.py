"""
File: app/schemas/report.py
Purpose: Pydantic models for report APIs.
Key classes: LearningReportRequest, LearningReportResponse.
Usage: Used by /api/reports endpoints.
"""
from pydantic import BaseModel


class LearningReportRequest(BaseModel):
    """Learning report request payload."""

    student_name: str
    key_points: list[str]
    weak_points: list[str]
    suggestions: str


class LearningReportResponse(BaseModel):
    """Learning report response payload."""

    report: str
