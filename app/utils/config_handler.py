"""
File: app/utils/config_handler.py
Purpose: Lightweight YAML config loader.
Key functions: load_yaml().
Usage: Used to load /config/*.yml files when needed.
"""
from pathlib import Path
from typing import Any
import yaml


def load_yaml(path: str) -> Any:
    """Load YAML config from a file path."""
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
