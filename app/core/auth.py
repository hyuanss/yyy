"""
File: app/core/auth.py
Purpose: API key authentication and role resolution.
Key functions/classes: verify_api_key(), get_user_role().
Usage: Added as dependency for API routers.
"""
from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.security import APIKeyHeader as RoleHeader

from app.core.config import settings
from app.db.repository import get_role_by_user_id
from app.db.session import SessionLocal
from app.core.roles import Role

_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
_role_header = RoleHeader(name="X-User-Role", auto_error=False)


def verify_api_key(api_key: str = Security(_api_key_header)) -> None:
    """Validate API key if configured; allow all if not set."""
    if not settings.api_key:
        return
    if api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="invalid api key")


def get_user_role(
    role_header: str = Security(_role_header),
    user_id: str | None = None,
) -> Role:
    """Resolve user role from header or database fallback."""
    if role_header:
        return Role(role_header)

    if SessionLocal and user_id:
        with SessionLocal() as db:
            role = get_role_by_user_id(db, user_id)
            if role:
                return Role(role)

    return Role.student
