"""
File: app/utils/file_handler.py
Purpose: Simple file operations for uploads or cached data.
Key functions: read_text(), write_text().
Usage: Can be used by services for file storage.
"""
from pathlib import Path


def read_text(path: str) -> str:
    """Read text content from a file path."""
    return Path(path).read_text(encoding="utf-8")


def write_text(path: str, content: str) -> None:
    """Write text content to a file path."""
    Path(path).write_text(content, encoding="utf-8")
