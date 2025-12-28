from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import get_settings
import logging

logger = logging.getLogger(__name__)

class DatabaseService:
    _engine = None
    _SessionLocal = None

    @classmethod
    def initialize(cls):
        settings = get_settings()
        
        try:
            cls._engine = create_engine(
                settings.DATABASE_URL,
                echo=settings.DEBUG,
                pool_pre_ping=True,
            )
            cls._SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=cls._engine,
            )
            logger.info("Database connection initialized")
        except Exception as e:
            logger.error(f"Database initialization error: {e}")
            raise

    @classmethod
    def get_db(cls) -> Session:
        if cls._SessionLocal is None:
            cls.initialize()
        
        db = cls._SessionLocal()
        try:
            yield db
        finally:
            db.close()

def get_db_session():
    """Dependency for getting DB session"""
    settings = get_settings()
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
