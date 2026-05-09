"""
Deprecated module.
Please import from top-level `utils` instead of `app.utils`.
This file is kept for backward compatibility.
"""
from utils.config_handler import (  # noqa: F401
    ConfigHandler,
    rag_conf,
    chroma_conf,
    prompts_conf,
    agent_conf,
)

__all__ = ["ConfigHandler", "rag_conf", "chroma_conf", "prompts_conf", "agent_conf"]
