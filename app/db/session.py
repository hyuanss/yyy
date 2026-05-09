"""
File: app/db/session.py
Purpose: SQLAlchemy session and engine initialization.
Key classes/methods: SessionLocal, Base, init_db().
Usage: Used by API endpoints to persist data.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings


DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL, pool_pre_ping=True) if DATABASE_URL else None
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) if engine else None
Base = declarative_base()


def init_db() -> None:
    """Initialize database tables if engine is configured."""
    if not engine:
        return
    Base.metadata.create_all(bind=engine)
