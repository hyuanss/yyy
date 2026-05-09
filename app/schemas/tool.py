"""
File: app/schemas/tool.py
Purpose: Pydantic models for tool endpoints.
Key classes: GradeHomeworkRequest/Response, GenerateQuizRequest/Response, GenerateLessonRequest/Response, GenerateReportRequest/Response.
Usage: Used by /api/tools endpoints.
"""
from pydantic import BaseModel


class GradeHomeworkRequest(BaseModel):
    """Homework grading request."""

    question: str
    answer: str


class GradeHomeworkResponse(BaseModel):
    """Homework grading response."""

    result: str


class GenerateQuizRequest(BaseModel):
    """Quiz generation request."""

    topic: str
    difficulty: str = "中等"


class GenerateQuizResponse(BaseModel):
    """Quiz generation response."""

    quiz: str


class GenerateLessonRequest(BaseModel):
    """Lesson plan request."""

    course: str
    objectives: list[str]


class GenerateLessonResponse(BaseModel):
    """Lesson plan response."""

    lesson: str


class GenerateReportRequest(BaseModel):
    """Report generation request."""

    summary: str


class GenerateReportResponse(BaseModel):
    """Report generation response."""

    report: str
