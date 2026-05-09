"""
File: app/schemas/chat.py
Purpose: Pydantic models for chat requests/responses.
Key classes: ChatRequest, ChatResponse.
Usage: Used by /api/chat endpoint.
"""
from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Chat request payload."""

    user_id: str
    message: str


class ChatResponse(BaseModel):
    """Chat response payload."""

    reply: str
