"""
File: app/services/report_service.py
Purpose: Report generation service for learning outcomes.
Key classes/methods: ReportService.generate_learning_report().
Usage: Used by /api/reports endpoints.
"""
from __future__ import annotations

from app.schemas.report import LearningReportRequest


class ReportService:
    """Generate structured learning reports with simple templates."""

    def generate_learning_report(self, payload: LearningReportRequest) -> str:
        """Return a formatted learning report based on input data."""
        points = "、".join(payload.key_points)
        weaknesses = "、".join(payload.weak_points)
        return (
            "学习报告\n"
            f"学习者: {payload.student_name}\n"
            f"关键掌握点: {points}\n"
            f"薄弱点: {weaknesses}\n"
            f"建议: {payload.suggestions}"
        )
