"""
File: app/api/chat.py
Purpose: Chat endpoints for the education agent.
Key functions/classes: chat_endpoint() uses AgentService.
Usage: POST /api/chat to get agent response.
"""
from fastapi import APIRouter, Depends, HTTPException

from app.core.auth import verify_api_key
from app.db.repository import save_chat_log
from app.db.session import SessionLocal
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import AgentService

router = APIRouter(tags=["chat"], dependencies=[Depends(verify_api_key)])
agent_service = AgentService()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest) -> ChatResponse:
    """Main chat endpoint that invokes the agent pipeline."""
    try:
        reply = agent_service.chat(user_id=payload.user_id, message=payload.message)
        if SessionLocal:
            with SessionLocal() as db:
                save_chat_log(db, payload.user_id, payload.message, reply)
        return ChatResponse(reply=reply)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"chat failed: {exc}") from exc
