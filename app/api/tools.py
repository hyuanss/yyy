"""
File: app/api/tools.py
Purpose: Tool endpoints (grading, quiz, lesson, report).
Key functions/classes: tool endpoints that call ToolService.
Usage: POST /api/tools/grade_homework etc.
"""
from fastapi import APIRouter, HTTPException

from app.schemas.tool import GradeHomeworkRequest, GradeHomeworkResponse
from app.schemas.tool import GenerateQuizRequest, GenerateQuizResponse
from app.schemas.tool import GenerateLessonRequest, GenerateLessonResponse
from app.schemas.tool import GenerateReportRequest, GenerateReportResponse
from app.services.tool_service import ToolService

router = APIRouter(tags=["tools"])
tool_service = ToolService()


@router.post("/tools/grade_homework", response_model=GradeHomeworkResponse)
def grade_homework(payload: GradeHomeworkRequest) -> GradeHomeworkResponse:
    """Grade student homework with simple rubric-based scoring."""
    try:
        result = tool_service.grade_homework(payload.question, payload.answer)
        return GradeHomeworkResponse(result=result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"grade_homework failed: {exc}") from exc


@router.post("/tools/generate_quiz", response_model=GenerateQuizResponse)
def generate_quiz(payload: GenerateQuizRequest) -> GenerateQuizResponse:
    """Generate a quiz based on a topic and difficulty level."""
    try:
        quiz = tool_service.generate_quiz(payload.topic, payload.difficulty)
        return GenerateQuizResponse(quiz=quiz)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"generate_quiz failed: {exc}") from exc


@router.post("/tools/generate_lesson", response_model=GenerateLessonResponse)
def generate_lesson(payload: GenerateLessonRequest) -> GenerateLessonResponse:
    """Generate a teaching lesson plan using a template."""
    try:
        lesson = tool_service.generate_lesson(payload.course, payload.objectives)
        return GenerateLessonResponse(lesson=lesson)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"generate_lesson failed: {exc}") from exc


@router.post("/tools/generate_report", response_model=GenerateReportResponse)
def generate_report(payload: GenerateReportRequest) -> GenerateReportResponse:
    """Generate a learning report from conversation summary."""
    try:
        report = tool_service.generate_report(payload.summary)
        return GenerateReportResponse(report=report)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"generate_report failed: {exc}") from exc
