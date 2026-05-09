"""
File: app/api/health.py
Purpose: Health check endpoint for service monitoring.
Key functions/classes: health_check().
Usage: GET /api/health for a simple status response.
"""
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict:
    """Return a simple health status payload."""
    return {"status": "ok"}
