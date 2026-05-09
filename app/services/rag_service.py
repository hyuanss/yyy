"""
File: app/services/rag_service.py
Purpose: RAG operations connected to existing VectorStoreService and RagSummarizeService.
Key classes/methods: RagService.query(), RagService.add_documents().
Usage: Used by /api/rag endpoints and agent tools.
"""
from __future__ import annotations

from typing import List

from langchain_core.documents import Document

from langchain.rag.vector_store import VectorStoreService
from langchain.rag.rag_service import RagSummarizeService


class RagService:
    """RAG service wrapper connecting to the existing LangChain RAG stack."""

    def __init__(self) -> None:
        self.vector_store = VectorStoreService()
        self.rag = RagSummarizeService(self.vector_store)

    def query(self, query: str, top_k: int = 3) -> str:
        """Query the knowledge base and return summarized context."""
        # RagSummarizeService internally uses retriever.k from config.
        return self.rag.rag_summarize(query)

    def add_documents(self, documents: List[str]) -> int:
        """Ingest raw text documents into the vector store."""
        # Convert raw strings into Document objects and split using the existing splitter.
        docs = [Document(page_content=doc) for doc in documents]
        split_docs = self.vector_store.spliter.split_documents(docs)
        if split_docs:
            self.vector_store.vector_store.add_documents(split_docs)
        return len(documents)
