from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from app.core.config import get_settings
from app.services.nlp_service import NLPService
from app.services.ml_service import MLService
from app.services.file_service import FileService
from app.models.schemas import MatchRequest, MatchResponse, MatchResult, SkillMatch
from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

# Initialize services
nlp_service = NLPService()
ml_service = MLService()
file_service = FileService()

# In-memory storage for demo (replace with DB in production)
uploaded_documents = {}

@router.post("/analyze")
async def analyze_match(request: MatchRequest, settings = Depends(get_settings)):
    """Perform semantic matching between resume and job description"""
    
    try:
        # Get documents (mock implementation - replace with DB queries)
        resume_path = Path(settings.UPLOAD_DIR) / f"{request.resume_id}.pdf"
        job_path = Path(settings.UPLOAD_DIR) / f"{request.job_id}.pdf"
        
        # For demo, we'll use sample texts
        resume_text = """Senior Software Engineer with 5 years of experience in Python,
        JavaScript, React, and FastAPI. Expert in machine learning and NLP.
        Worked on distributed systems and microservices."""
        
        job_text = """We are hiring a Software Engineer with:
        - 3+ years Python experience
        - React and JavaScript skills required
        - Machine Learning knowledge preferred
        - Experience with FastAPI or similar frameworks"""
        
        # Process documents with NLP
        resume_processed = nlp_service.process_document(resume_text, "resume")
        job_processed = nlp_service.process_document(job_text, "job_description")
        
        # Extract skills
        resume_skills = resume_processed['skills']
        job_skills = job_processed['skills']
        
        # Skill matching
        skill_match = ml_service.match_skills(job_skills, resume_skills)
        
        # Semantic similarity
        semantic_score = ml_service.semantic_similarity(resume_text, job_text)
        
        # Experience matching (mock)
        resume_years_min, resume_years_max = resume_processed['experience_years']
        experience_match = resume_years_min >= 3  # Job requires 3+ years
        
        # Education matching (mock)
        education_match = True
        
        # Calculate overall score
        match_score = ml_service.calculate_match_score(
            semantic_score,
            skill_match['match_percentage'] / 100,
            experience_match,
            education_match
        )
        
        # Generate recommendations
        recommendations = ml_service.generate_recommendations(
            match_score,
            skill_match['missing_skills'],
            1 - skill_match['match_percentage'] / 100
        )
        
        # Create response
        match_result = MatchResult(
            match_score=round(match_score, 2),
            similarity_score=round(semantic_score, 3),
            matched_skills=[
                SkillMatch(skill=s, matched=True)
                for s in skill_match['matched_skills']
            ],
            missing_skills=skill_match['missing_skills'],
            experience_match=experience_match,
            education_match=education_match,
            explanation=f"Resume shows {skill_match['match_percentage']:.0f}% skill match with semantic similarity of {semantic_score:.2f}",
            timestamp=datetime.now()
        )
        
        logger.info(f"Match analysis completed: {request.resume_id} vs {request.job_id}")
        
        return MatchResponse(
            resume_id=request.resume_id,
            job_id=request.job_id,
            results=match_result,
            recommendations=recommendations
        )
    
    except Exception as e:
        logger.error(f"Error during matching: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Check if matching service is healthy"""
    return {
        "status": "operational",
        "services": {
            "nlp": "ready",
            "ml": "ready",
            "file_processor": "ready"
        }
    }
