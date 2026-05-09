"""
File: app/utils/logger_handler.py
Purpose: Create module-specific loggers.
Key functions: get_logger().
Usage: Used across services for consistent logging.
"""
import logging


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger."""
    return logging.getLogger(name)
