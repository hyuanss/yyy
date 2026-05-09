"""
File: app/services/agent_service.py
Purpose: Agent orchestration bridging FastAPI with LangChain ReactAgent.
Key classes/methods: AgentService.chat().
Usage: Called by /api/chat endpoint to return a full response string.
"""
from __future__ import annotations

from langchain.agent.react_agent import ReactAgent


class AgentService:
    """High-level agent orchestration service."""

    def __init__(self) -> None:
        # Initialize the LangChain ReactAgent once for reuse.
        self._agent = ReactAgent()

    def chat(self, user_id: str, message: str) -> str:
        """Generate an agent response using the existing ReactAgent stream."""
        # Collect streaming chunks into a single response.
        chunks: list[str] = []
        for chunk in self._agent.execute_stream(message):
            chunks.append(chunk)
        return "".join(chunks).strip()
