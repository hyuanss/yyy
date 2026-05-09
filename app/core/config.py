"""
File: app/core/config.py
Purpose: Configuration management using environment variables and optional YAML.
Key classes/methods: Settings.
Usage: Imported by services and app for config.
"""
from __future__ import annotations

import os
from typing import Any, Dict

import yaml
from pydantic import BaseSettings

from utils.path_tools import get_abs_path


def _load_mysql_config() -> Dict[str, Any]:
    """Load MySQL settings from config/mysql.yml if available."""
    config_path = get_abs_path("config/mysql.yml")
    if not os.path.exists(config_path):
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f.read()) or {}


class Settings(BaseSettings):
    """Application settings loaded from environment or config/mysql.yml."""

    app_name: str = "Edu Agent System"
    log_level: str = "INFO"
    api_key: str = os.getenv("EDU_API_KEY", "")

    @property
    def database_url(self) -> str:
        """Build a SQLAlchemy database URL from env or config/mysql.yml."""
        env_url = os.getenv("EDU_DATABASE_URL", "")
        if env_url:
            return env_url

        mysql_conf = _load_mysql_config()
        if not mysql_conf:
            return ""

        user = mysql_conf.get("user", "root")
        password = mysql_conf.get("password", "")
        host = mysql_conf.get("host", "localhost")
        port = mysql_conf.get("port", 3306)
        database = mysql_conf.get("database", "edu_agent")
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4"

    class Config:
        env_prefix = "EDU_"


settings = Settings()
