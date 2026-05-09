"""
File: app/db/repository.py
Purpose: Data persistence helper functions.
Key functions: save_chat_log(), save_report_log().
Usage: Called by API endpoints after generating results.
"""
from typing import List

from sqlalchemy.orm import Session

from app.db.models import ChatLog, ReportLog


def save_chat_log(db: Session, user_id: str, message: str, reply: str) -> None:
    """Persist a chat log record."""
    db.add(ChatLog(user_id=user_id, message=message, reply=reply))
    db.commit()


def save_report_log(
    db: Session,
    student_name: str,
    key_points: List[str],
    weak_points: List[str],
    suggestions: str,
    report: str,
) -> None:
    """Persist a learning report record."""
    db.add(
        ReportLog(
            student_name=student_name,
            key_points=",".join(key_points),
            weak_points=",".join(weak_points),
            suggestions=suggestions,
            report=report,
        )
    )
    db.commit()
