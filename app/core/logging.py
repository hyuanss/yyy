"""
File: app/core/logging.py
Purpose: Centralized logging configuration.
Key functions: setup_logging().
Usage: Called by app.main during startup.
"""
import logging

from app.core.config import settings


def setup_logging() -> None:
    """Initialize structured logging for the application."""
    logging.basicConfig(
        level=settings.log_level,
        format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
    )
