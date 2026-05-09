"""
File: app/main.py
Purpose: FastAPI application entrypoint and router wiring.
Key functions/classes: create_app() and app instance.
Usage: Run with `uvicorn app.main:app --reload`.
"""
from fastapi import FastAPI

from app.api import chat, rag, tools, reports
from app.core.logging import setup_logging


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    setup_logging()
    application = FastAPI(title="Edu Agent System", version="0.1.0")

    # Register API routers.
    application.include_router(chat.router, prefix="/api")
    application.include_router(rag.router, prefix="/api")
    application.include_router(tools.router, prefix="/api")
    application.include_router(reports.router, prefix="/api")

    return application


# Exposed app instance for ASGI servers like Uvicorn.
app = create_app()
