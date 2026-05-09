"""
File: app/utils/chain_debug.py
Purpose: Debug helper for chain outputs.
Key functions: format_debug().
Usage: Used during development to inspect intermediate results.
"""
from typing import Any


def format_debug(data: Any) -> str:
    """Format debug information into a readable string."""
    return f"[DEBUG] {data!r}"
