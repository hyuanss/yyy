"""
File: app/services/agent_service.py
Purpose: Agent orchestration combining RAG and tools.
Key classes/methods: AgentService.chat().
Usage: Called by /api/chat endpoint.
"""
from __future__ import annotations

from app.services.rag_service import RagService
from app.services.tool_service import ToolService


class AgentService:
    """High-level agent orchestration service."""

    def __init__(self) -> None:
        self.rag_service = RagService()
        self.tool_service = ToolService()

    def chat(self, user_id: str, message: str) -> str:
        """Generate an agent response using RAG context and tools when needed."""
        # Step 1: Retrieve context from RAG.
        context = self.rag_service.query(query=message, top_k=3)

        # Step 2: Basic routing to tools by simple keywords (lightweight, easy to extend).
        if "作业" in message or "批改" in message:
            return self.tool_service.grade_homework("自动识别题目", message)
        if "出题" in message or "测试题" in message:
            return self.tool_service.generate_quiz("自动识别主题", "中等")
        if "教案" in message:
            return self.tool_service.generate_lesson("自动识别课程", ["目标1", "目标2"])

        # Step 3: Default chat response using RAG context.
        return (
            "【教育智能体答复】\n"
            f"问题: {message}\n"
            f"参考资料: {context}\n"
            "建议: 如需更具体的教学内容，请提供年级与课程主题。"
        )
