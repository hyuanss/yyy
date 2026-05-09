"""
File: app/db/models.py
Purpose: ORM models for chat logs, reports, users, and memory summaries.
Key classes: ChatLog, ReportLog, User, MemorySummary.
Usage: Used by repository helpers to save data.
"""
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.db.session import Base


class User(Base):
    """User model with role field for access control."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(64), unique=True, index=True, nullable=False)
    role = Column(String(32), nullable=False, default="student")


class ChatLog(Base):
    """Chat log model for persisting conversations."""

    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(64), index=True, nullable=False)
    message = Column(Text, nullable=False)
    reply = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ReportLog(Base):
    """Learning report model for persisting generated reports."""

    __tablename__ = "report_logs"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(128), nullable=False)
    key_points = Column(Text, nullable=False)
    weak_points = Column(Text, nullable=False)
    suggestions = Column(Text, nullable=False)
    report = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class MemorySummary(Base):
    """Long-term memory summary for a user."""

    __tablename__ = "memory_summaries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(64), unique=True, index=True, nullable=False)
    summary = Column(Text, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
