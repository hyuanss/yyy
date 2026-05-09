"""
File: app/main.py
Purpose: FastAPI application entrypoint and router wiring.
Key functions/classes: create_app() and app instance.
Usage: Run with `uvicorn app.main:app --reload`.
"""
from fastapi import FastAPI

from app.api import chat, rag, tools, reports, health
from app.core.logging import setup_logging
from langchain.rag.vector_store import VectorStoreService


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    setup_logging()
    application = FastAPI(title="Edu Agent System", version="0.1.0")

    # Register API routers.
    application.include_router(chat.router, prefix="/api")
    application.include_router(rag.router, prefix="/api")
    application.include_router(tools.router, prefix="/api")
    application.include_router(reports.router, prefix="/api")
    application.include_router(health.router, prefix="/api")

    @application.on_event("startup")
    def load_knowledge_base() -> None:
        """Load knowledge documents into the vector store on startup."""
        VectorStoreService().load_document()

    return application


# Exposed app instance for ASGI servers like Uvicorn.
app = create_app()
