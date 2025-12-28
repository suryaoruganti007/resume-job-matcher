from sqlalchemy import Column, String, DateTime, Float, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String, nullable=False)
    extracted_text = Column(Text)
    skills = Column(Text)  # JSON string
    experience_years = Column(Integer)
    upload_timestamp = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String, nullable=False)
    extracted_text = Column(Text)
    required_skills = Column(Text)  # JSON string
    experience_required = Column(Integer)
    upload_timestamp = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

class MatchResult(Base):
    __tablename__ = "match_results"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    resume_id = Column(String, nullable=False)
    job_id = Column(String, nullable=False)
    match_score = Column(Float)
    similarity_score = Column(Float)
    matched_skills = Column(Text)  # JSON string
    missing_skills = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
