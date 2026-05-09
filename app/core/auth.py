"""
File: app/core/auth.py
Purpose: API key authentication dependency.
Key functions/classes: verify_api_key().
Usage: Added as dependency for API routers.
"""
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

from app.core.config import settings

_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def verify_api_key(api_key: str = Security(_api_key_header)) -> None:
    """Validate API key if configured; allow all if not set."""
    if not settings.api_key:
        return
    if api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="invalid api key")
