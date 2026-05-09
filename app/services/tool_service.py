"""
File: app/services/tool_service.py
Purpose: Tool execution service wired to existing agent tools.
Key classes/methods: ToolService.grade_homework(), generate_quiz(), generate_lesson(), generate_report().
Usage: Used by /api/tools endpoints and AgentService.
"""
from __future__ import annotations

from langchain.agent.tools.agent_tools import (
    get_weather,
    get_user_location,
    get_user_id,
    get_current_month,
)


class ToolService:
    """Tool execution layer that wraps existing tool functions."""

    def grade_homework(self, question: str, answer: str) -> str:
        """Return a simple rubric-based evaluation result."""
        # Placeholder: keep a simple deterministic output for now.
        score = 85 if len(answer) > 20 else 60
        return f"题目: {question}\n评分: {score}/100\n点评: 回答结构清晰，可加强例子与推导。"

    def generate_quiz(self, topic: str, difficulty: str) -> str:
        """Generate a short quiz template for the given topic."""
        return (
            f"主题: {topic}\n难度: {difficulty}\n"
            "1) 简答题：请解释核心概念。\n"
            "2) 判断题：概念A与概念B是否等价？\n"
            "3) 应用题：给出一个真实场景进行分析。"
        )

    def generate_lesson(self, course: str, objectives: list[str]) -> str:
        """Generate a compact lesson plan using a fixed template."""
        objectives_text = "、".join(objectives)
        return (
            f"课程: {course}\n"
            f"教学目标: {objectives_text}\n"
            "流程: 导入(5min) -> 讲解(20min) -> 练习(15min) -> 总结(5min)"
        )

    def generate_report(self, summary: str) -> str:
        """Generate a learning report from a summary text."""
        return (
            "学习报告\n"
            f"学习摘要: {summary}\n"
            "建议: 复习关键概念并完成对应练习。"
        )

    def get_weather(self, city: str) -> str:
        """Expose weather tool for testing."""
        return get_weather(city)

    def get_user_location(self) -> str:
        """Expose user location tool for testing."""
        return get_user_location()

    def get_user_id(self) -> str:
        """Expose user id tool for testing."""
        return get_user_id()

    def get_current_month(self) -> str:
        """Expose current month tool for testing."""
        return get_current_month()
