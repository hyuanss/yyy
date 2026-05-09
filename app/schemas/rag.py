"""
File: app/schemas/rag.py
Purpose: Pydantic models for RAG queries and uploads.
Key classes: RagQueryRequest, RagQueryResponse, RagUploadRequest, RagUploadResponse.
Usage: Used by /api/rag endpoints.
"""
from typing import List
from pydantic import BaseModel


class RagQueryRequest(BaseModel):
    """RAG query request payload."""

    query: str
    top_k: int = 3


class RagQueryResponse(BaseModel):
    """RAG query response payload."""

    context: str


class RagUploadRequest(BaseModel):
    """RAG document upload payload."""

    documents: List[str]


class RagUploadResponse(BaseModel):
    """RAG upload response payload."""

    ingested: int
