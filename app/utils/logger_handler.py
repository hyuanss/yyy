"""
Deprecated module.
Please import from top-level `utils` instead of `app.utils`.
This file is kept for backward compatibility.
"""
from utils.logger_handler import (  # noqa: F401
    get_logger,
    logger,
    mask_sensitive_data,
    SensitiveDataFilter,
)

__all__ = ["get_logger", "logger", "mask_sensitive_data", "SensitiveDataFilter"]
