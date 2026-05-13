import os
import requests
import streamlit as st

# =========================
# 基础配置
# =========================
st.set_page_config(
    page_title="教育智能体系统",
    layout="wide"
)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api")
API_KEY = os.getenv("EDU_API_KEY", "")


# =========================
# 角色映射（解决中文 header 报错）
# =========================
ROLE_MAP = {
    "学生": "student",
    "教师": "teacher"
}


# =========================
# 请求头
# =========================
def _headers(role: str) -> dict:
    headers = {
        "X-User-Role": role
    }

    if API_KEY:
        headers["X-API-Key"] = API_KEY

    return headers


# =========================
# 初始化 session_state
# =========================
if "chat_ids" not in st.session_state:
    st.session_state.chat_ids = ["会话1"]

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "会话1"

if "chat_histories" not in st.session_state:
    st.session_state.chat_histories = {}

if "selected_tool" not in st.session_state:
    st.session_state.selected_tool = None


# =========================
# 聊天模块
# =========================
def chat_ui(role: str, chat_id: str):

    # 初始化当前会话
    if chat_id not in st.session_state.chat_histories:
        st.session_state.chat_histories[chat_id] = []

    chat_history = st.session_state.chat_histories[chat_id]

    # =========================
    # 聊天记录区域
    # =========================
    chat_container = st.container()

    with chat_container:
        for msg in chat_history:

            if msg["role"] == "user":
                with st.chat_message("user"):
                    st.write(msg["content"])

            else:
                with st.chat_message("assistant"):
                    st.write(msg["content"])

    st.divider()

    # =========================
    # 输入区域（固定在下方）
    # =========================
    with st.form(
        key=f"chat_form_{chat_id}",
        clear_on_submit=True
    ):

        user_message = st.text_area(
            "请输入问题",
            height=80,
            placeholder="请输入你的问题..."
        )

        submitted = st.form_submit_button("发送")

        if submitted and user_message.strip():

            # 用户消息
            chat_history.append({
                "role": "user",
                "content": user_message
            })

            try:

                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={
                        "user_id": "student_001",
                        "message": user_message
                    },
                    headers=_headers(role),
                    timeout=30,
                )

                # =========================
                # 调试输出（终端可见）
                # =========================
                print("状态码:", response.status_code)
                print("返回内容:", response.text)

                # =========================
                # 正常响应
                # =========================
                if response.status_code == 200:

                    try:
                        reply = response.json().get("reply", "")

                    except Exception:
                        reply = response.text

                else:
                    reply = (
                        f"后端错误: {response.status_code}\n\n"
                        f"{response.text}"
                    )

            except Exception as e:

                reply = f"请求失败:\n{str(e)}"

            # AI 回复
            chat_history.append({
                "role": "assistant",
                "content": reply
            })

            # 强制刷新页面
            st.rerun()


# =========================
# 教学工具模块
# =========================
def tools_ui(role: str):

    st.subheader("教学工具")

    # =========================
    # 四个工具卡片
    # =========================
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📝 作业批改", use_container_width=True):
            st.session_state.selected_tool = "grade_homework"

    with col2:
        if st.button("📚 自动出题", use_container_width=True):
            st.session_state.selected_tool = "generate_quiz"

    with col3:
        if st.button("📖 教案生成", use_container_width=True):
            st.session_state.selected_tool = "generate_lesson"

    with col4:
        if st.button("📊 报告生成", use_container_width=True):
            st.session_state.selected_tool = "generate_report"

    st.divider()

    tool = st.session_state.selected_tool

    # =========================
    # 作业批改
    # =========================
    if tool == "grade_homework":

        st.subheader("作业批改")

        question = st.text_input("题目")
        answer = st.text_area("学生答案")

        if st.button("开始批改"):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/tools/grade_homework",
                    json={
                        "question": question,
                        "answer": answer
                    },
                    headers=_headers(role),
                    timeout=30,
                )

                st.success(response.json().get("result", ""))

            except Exception as e:
                st.error(str(e))

    # =========================
    # 自动出题
    # =========================
    elif tool == "generate_quiz":

        st.subheader("自动出题")

        topic = st.text_input("主题")

        difficulty = st.selectbox(
            "难度",
            ["简单", "中等", "困难"]
        )

        if st.button("生成题目"):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/tools/generate_quiz",
                    json={
                        "topic": topic,
                        "difficulty": difficulty
                    },
                    headers=_headers(role),
                    timeout=30,
                )

                st.success(response.json().get("quiz", ""))

            except Exception as e:
                st.error(str(e))

    # =========================
    # 教案生成
    # =========================
    elif tool == "generate_lesson":

        st.subheader("教案生成")

        course = st.text_input("课程")

        objectives = st.text_area(
            "教学目标（逗号分隔）"
        )

        if st.button("生成教案"):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/tools/generate_lesson",
                    json={
                        "course": course,
                        "objectives": [
                            o.strip()
                            for o in objectives.split(",")
                            if o.strip()
                        ]
                    },
                    headers=_headers(role),
                    timeout=30,
                )

                st.success(response.json().get("lesson", ""))

            except Exception as e:
                st.error(str(e))

    # =========================
    # 报告生成
    # =========================
    elif tool == "generate_report":

        st.subheader("报告生成")

        summary = st.text_area("学习摘要")

        if st.button("生成报告"):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/tools/generate_report",
                    json={
                        "summary": summary
                    },
                    headers=_headers(role),
                    timeout=30,
                )

                st.success(response.json().get("report", ""))

            except Exception as e:
                st.error(str(e))


# =========================
# 左侧边栏
# =========================
with st.sidebar:

    st.title("教育智能体")

    # 中文显示
    role_cn = st.selectbox(
        "选择角色",
        ["学生", "教师"]
    )

    # 英文传给后端
    role = ROLE_MAP[role_cn]

    user_email = "123@123.com"

    st.markdown(f"### {role_cn}")
    st.caption(user_email)

    st.divider()

    # =========================
    # 新建会话
    # =========================
    if st.button(
        "➕ 新建会话",
        use_container_width=True
    ):

        new_chat = f"会话{len(st.session_state.chat_ids) + 1}"

        st.session_state.chat_ids.append(new_chat)

        st.session_state.current_chat = new_chat

        st.rerun()

    st.markdown("### 历史会话")

    # =========================
    # 历史记录
    # =========================
    for chat_id in st.session_state.chat_ids:

        if st.button(
            chat_id,
            key=chat_id,
            use_container_width=True
        ):

            st.session_state.current_chat = chat_id

            st.rerun()


# =========================
# 主页面
# =========================
st.title("教育智能体系统")

st.caption(f"当前会话：{st.session_state.current_chat}")

# =========================
# 功能切换
# =========================
tab = st.radio(
    "功能选择",
    ["智能答疑", "教学工具"],
    horizontal=True
)

st.divider()

# =========================
# 页面内容
# =========================
if tab == "智能答疑":

    chat_ui(
        role,
        st.session_state.current_chat
    )

elif tab == "教学工具":

    tools_ui(role)
