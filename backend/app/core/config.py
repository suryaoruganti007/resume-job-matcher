from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application configuration"""
    
    # App settings
    APP_NAME: str = "Resume-Job Matcher API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # API settings
    API_PREFIX: str = "/api"
    
    # Database
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # File uploads
    MAX_UPLOAD_SIZE: int = 52428800  # 50MB
    UPLOAD_DIR: str = "./uploads"
    ALLOWED_EXTENSIONS: List[str] = ["pdf", "docx"]
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000"
    ]
    
    # NLP/ML models
    SPACY_MODEL: str = "en_core_web_sm"
    SBERT_MODEL: str = "all-MiniLM-L6-v2"
    
    # Allow extra env vars (fixes the error)
    model_config = {
        "extra": "ignore",  # Ignore extra fields like FASTAPI_ENV
        "env_file": ".env"
    }

def get_settings() -> Settings:
    return Settings()
