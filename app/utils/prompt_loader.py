"""
File: app/utils/prompt_loader.py
Purpose: Load prompt templates from disk.
Key functions: load_prompt().
Usage: Used by services when constructing prompts.
"""
from pathlib import Path


def load_prompt(path: str) -> str:
    """Load a prompt template from the given file path."""
    return Path(path).read_text(encoding="utf-8")
