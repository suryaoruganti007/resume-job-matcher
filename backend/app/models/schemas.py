from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class FileUploadResponse(BaseModel):
    """Response after file upload"""
    file_id: str
    filename: str
    file_type: str  # 'resume' or 'job_description'
    upload_timestamp: datetime
    extracted_text: Optional[str] = None
    
    class Config:
        from_attributes = True

class MatchRequest(BaseModel):
    """Request to perform matching"""
    resume_id: str
    job_id: str
    
    class Config:
        from_attributes = True

class SkillMatch(BaseModel):
    """Individual skill match"""
    skill: str
    matched: bool
    frequency: int = Field(default=1)

class MatchResult(BaseModel):
    """Result of resume-job matching"""
    match_score: float = Field(..., ge=0, le=100)
    similarity_score: float = Field(..., ge=0, le=1)
    matched_skills: List[SkillMatch]
    missing_skills: List[str]
    experience_match: bool
    education_match: bool
    explanation: str
    timestamp: datetime

class MatchResponse(BaseModel):
    """API response for match results"""
    resume_id: str
    job_id: str
    results: MatchResult
    recommendations: List[str] = []
