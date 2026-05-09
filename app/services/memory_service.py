"""
File: app/services/memory_service.py
Purpose: Manage short-term and long-term memory for users.
Key classes/methods: MemoryService.get_memory(), update_memory().
Usage: Called by API endpoints and AgentService.
"""
from __future__ import annotations

from typing import List

from sqlalchemy.orm import Session

from app.db.models import ChatLog
from app.db.repository import get_memory_summary, upsert_memory_summary


class MemoryService:
    """Simple memory manager using recent logs and long-term summaries."""

    def __init__(self, short_term_limit: int = 5) -> None:
        self.short_term_limit = short_term_limit

    def get_short_term(self, db: Session, user_id: str) -> List[ChatLog]:
        """Return the latest chat logs for a user."""
        return (
            db.query(ChatLog)
            .filter(ChatLog.user_id == user_id)
            .order_by(ChatLog.created_at.desc())
            .limit(self.short_term_limit)
            .all()
        )

    def get_memory(self, db: Session, user_id: str) -> str:
        """Return combined long-term summary and short-term context."""
        summary = get_memory_summary(db, user_id) or ""
        logs = self.get_short_term(db, user_id)
        short_term = "\n".join(
            [f"用户: {log.message}\n助手: {log.reply}" for log in reversed(logs)]
        )
        if summary and short_term:
            return f"历史摘要: {summary}\n最近对话:\n{short_term}"
        if summary:
            return f"历史摘要: {summary}"
        return short_term

    def update_memory(self, db: Session, user_id: str) -> None:
        """Update long-term summary using recent logs (simple heuristic)."""
        logs = self.get_short_term(db, user_id)
        if not logs:
            return
        # Simple summary heuristic: concatenate recent messages with truncation.
        summary_text = " | ".join([f"{log.message}->{log.reply}" for log in reversed(logs)])
        summary_text = summary_text[:500]
        upsert_memory_summary(db, user_id, summary_text)
