"""
File: app/api/rag.py
Purpose: RAG endpoints for querying and uploading documents.
Key functions/classes: rag_query(), rag_upload().
Usage: POST /api/rag/query or /api/rag/upload.
"""
from fastapi import APIRouter, HTTPException

from app.schemas.rag import RagQueryRequest, RagQueryResponse, RagUploadRequest, RagUploadResponse
from app.services.rag_service import RagService

router = APIRouter(tags=["rag"])
rag_service = RagService()


@router.post("/rag/query", response_model=RagQueryResponse)
def rag_query(payload: RagQueryRequest) -> RagQueryResponse:
    """Query the RAG system and return relevant context."""
    try:
        context = rag_service.query(query=payload.query, top_k=payload.top_k)
        return RagQueryResponse(context=context)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"rag query failed: {exc}") from exc


@router.post("/rag/upload", response_model=RagUploadResponse)
def rag_upload(payload: RagUploadRequest) -> RagUploadResponse:
    """Upload documents into the RAG knowledge base."""
    try:
        count = rag_service.add_documents(documents=payload.documents)
        return RagUploadResponse(ingested=count)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"rag upload failed: {exc}") from exc
