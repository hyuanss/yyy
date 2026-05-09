"""
File: app/core/roles.py
Purpose: Role definitions and access control helpers.
Key classes/functions: Role, require_role().
Usage: Applied as FastAPI dependencies to protect endpoints.
"""
from enum import Enum

from fastapi import Depends, HTTPException

from app.core.auth import get_user_role


class Role(str, Enum):
    """Supported user roles."""

    student = "student"
    teacher = "teacher"
    admin = "admin"


def require_role(required: Role):
    """Return a dependency that enforces the required role."""

    def _checker(role: Role = Depends(get_user_role)) -> None:
        if role != required and role != Role.admin:
            raise HTTPException(status_code=403, detail="forbidden")

    return _checker
