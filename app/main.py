"""
File: app/main.py
Purpose: FastAPI application entrypoint and router wiring.
Key functions/classes: create_app() and app instance.
Usage: Run with `uvicorn app.main:app --reload`.
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.api import chat, rag, tools, reports, health
from app.core.errors import ErrorResponse
from app.core.logging import setup_logging
from app.db.session import init_db
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
        """Load knowledge documents and initialize DB on startup."""
        init_db()
        VectorStoreService().load_document()

    @application.exception_handler(HTTPException)
    def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
        """Return unified error response for HTTP exceptions."""
        payload = ErrorResponse(error_code="http_error", message=str(exc.detail))
        return JSONResponse(status_code=exc.status_code, content=payload.model_dump())

    @application.exception_handler(Exception)
    def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        """Return unified error response for unhandled exceptions."""
        payload = ErrorResponse(error_code="internal_error", message=str(exc))
        return JSONResponse(status_code=500, content=payload.model_dump())

    return application


# Exposed app instance for ASGI servers like Uvicorn.
app = create_app()
