"""
File: app/db/repository.py
Purpose: Data persistence helper functions.
Key functions: save_chat_log(), save_report_log(), get_role_by_user_id(), upsert_memory_summary().
Usage: Called by API endpoints after generating results.
"""
from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models import ChatLog, ReportLog, User, MemorySummary


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


def get_role_by_user_id(db: Session, user_id: str) -> Optional[str]:
    """Fetch role by user_id if exists."""
    record = db.query(User).filter(User.user_id == user_id).first()
    return record.role if record else None


def upsert_memory_summary(db: Session, user_id: str, summary: str) -> None:
    """Insert or update memory summary for a user."""
    record = db.query(MemorySummary).filter(MemorySummary.user_id == user_id).first()
    if record:
        record.summary = summary
    else:
        db.add(MemorySummary(user_id=user_id, summary=summary))
    db.commit()


def get_memory_summary(db: Session, user_id: str) -> Optional[str]:
    """Get stored memory summary for a user."""
    record = db.query(MemorySummary).filter(MemorySummary.user_id == user_id).first()
    return record.summary if record else None
