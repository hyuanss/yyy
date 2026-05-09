"""
File: app/services/agent_service.py
Purpose: Agent orchestration bridging FastAPI with LangChain ReactAgent.
Key classes/methods: AgentService.chat().
Usage: Called by /api/chat endpoint to return a full response string.
"""
from __future__ import annotations

from langchain.agent.react_agent import ReactAgent

from app.services.memory_service import MemoryService
from app.db.session import SessionLocal


class AgentService:
    """High-level agent orchestration service."""

    def __init__(self) -> None:
        # Initialize the LangChain ReactAgent once for reuse.
        self._agent = ReactAgent()
        self._memory_service = MemoryService()

    def chat(self, user_id: str, message: str) -> str:
        """Generate an agent response using memory-augmented input."""
        memory = ""
        if SessionLocal:
            with SessionLocal() as db:
                memory = self._memory_service.get_memory(db, user_id)

        prompt = message
        if memory:
            prompt = f"{memory}\n用户问题: {message}"

        # Collect streaming chunks into a single response.
        chunks: list[str] = []
        for chunk in self._agent.execute_stream(prompt):
            chunks.append(chunk)
        return "".join(chunks).strip()
