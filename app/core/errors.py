"""
File: app/core/errors.py
Purpose: Unified error response schema.
Key classes: ErrorResponse.
Usage: Used by exception handlers in app.main.
"""
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Standard error response model."""

    error_code: str
    message: str
