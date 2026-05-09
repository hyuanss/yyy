"""
File: app/services/rag_service.py
Purpose: RAG operations such as query and document ingestion.
Key classes/methods: RagService.query(), RagService.add_documents().
Usage: Used by AgentService and /api/rag endpoints.
"""
from __future__ import annotations

from typing import List


class RagService:
    """Lightweight RAG service wrapper (can be replaced by real vector store)."""

    def __init__(self) -> None:
        # In a production system, you would initialize vector store here.
        self._memory_store: List[str] = []

    def query(self, query: str, top_k: int = 3) -> str:
        """Query the knowledge base and return concatenated context."""
        # Simplified retrieval: return last documents for now.
        if not self._memory_store:
            return "暂无知识库内容，可先上传教材或课堂资料。"
        return " | ".join(self._memory_store[-top_k:])

    def add_documents(self, documents: List[str]) -> int:
        """Ingest documents into the in-memory knowledge base."""
        self._memory_store.extend(documents)
        return len(documents)
