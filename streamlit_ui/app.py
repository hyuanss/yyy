import os
import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api")
API_KEY = os.getenv("EDU_API_KEY", "")


def _headers(role: str) -> dict:
    """Prepare request headers with API key and role if configured."""
    headers = {"X-User-Role": role}
    if API_KEY:
        headers["X-API-Key"] = API_KEY
    return headers


def render_chat(role: str) -> None:
    """Render the chat UI."""
    st.subheader("智能答疑")
    user_id = st.text_input("用户ID", value="student_001")
    message = st.text_area("请输入问题")
    if st.button("发送"):
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={"user_id": user_id, "message": message},
            headers=_headers(role),
            timeout=30,
        )
        st.write(response.json().get("reply", ""))


def render_tools(role: str) -> None:
    """Render tool-related UI."""
    st.subheader("教学工具")
    tool = st.selectbox("选择工具", ["作业批改", "自动出题", "教案生成", "报告生成"])

    if tool == "作业批改":
        question = st.text_input("题目")
        answer = st.text_area("学生答案")
        if st.button("批改"):
            response = requests.post(
                f"{BACKEND_URL}/tools/grade_homework",
                json={"question": question, "answer": answer},
                headers=_headers(role),
                timeout=30,
            )
            st.write(response.json().get("result", ""))

    if tool == "自动出题":
        topic = st.text_input("主题")
        difficulty = st.selectbox("难度", ["简单", "中等", "困难"])
        if st.button("生成题目"):
            response = requests.post(
                f"{BACKEND_URL}/tools/generate_quiz",
                json={"topic": topic, "difficulty": difficulty},
                headers=_headers(role),
                timeout=30,
            )
            st.write(response.json().get("quiz", ""))

    if tool == "教案生成":
        course = st.text_input("课程")
        objectives = st.text_area("教学目标(用逗号分隔)")
        if st.button("生成教案"):
            response = requests.post(
                f"{BACKEND_URL}/tools/generate_lesson",
                json={"course": course, "objectives": [o.strip() for o in objectives.split(",") if o.strip()]},
                headers=_headers(role),
                timeout=30,
            )
            st.write(response.json().get("lesson", ""))

    if tool == "报告生成":
        summary = st.text_area("学习摘要")
        if st.button("生成报告"):
            response = requests.post(
                f"{BACKEND_URL}/tools/generate_report",
                json={"summary": summary},
                headers=_headers(role),
                timeout=30,
            )
            st.write(response.json().get("report", ""))


def render_reports(role: str) -> None:
    """Render structured report UI."""
    st.subheader("学习报告")
    student_name = st.text_input("学生姓名")
    key_points = st.text_input("关键掌握点(逗号分隔)")
    weak_points = st.text_input("薄弱点(逗号分隔)")
    suggestions = st.text_area("建议")
    if st.button("生成学习报告"):
        response = requests.post(
            f"{BACKEND_URL}/reports/learning",
            json={
                "student_name": student_name,
                "key_points": [p.strip() for p in key_points.split(",") if p.strip()],
                "weak_points": [p.strip() for p in weak_points.split(",") if p.strip()],
                "suggestions": suggestions,
            },
            headers=_headers(role),
            timeout=30,
        )
        st.write(response.json().get("report", ""))


st.title("教育智能体系统")
role = st.sidebar.selectbox("角色", ["student", "teacher", "admin"])
section = st.sidebar.radio("功能", ["智能答疑", "教学工具", "学习报告"])

if section == "智能答疑":
    render_chat(role)
elif section == "教学工具":
    render_tools(role)
else:
    render_reports(role)
