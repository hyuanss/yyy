"""
Deprecated module.
Please import from top-level `utils` instead of `app.utils`.
This file is kept for backward compatibility.
"""
from utils.prompt_loader import load_system_prompt, load_report_prompt

__all__ = ["load_system_prompt", "load_report_prompt"]
