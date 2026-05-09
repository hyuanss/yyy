"""
File: app/core/config.py
Purpose: Configuration management using environment variables.
Key classes/methods: Settings.
Usage: Imported by services and app for config.
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment."""

    app_name: str = "Edu Agent System"
    log_level: str = "INFO"

    class Config:
        env_prefix = "EDU_"


settings = Settings()
