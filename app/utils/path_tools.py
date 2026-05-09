"""
File: app/utils/path_tools.py
Purpose: Path helpers for resolving project-relative directories.
Key functions: project_root().
Usage: Used by services for locating config/prompts.
"""
from pathlib import Path


def project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parents[2]
