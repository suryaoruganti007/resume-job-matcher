from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)

class MLService:
    """Machine Learning service for semantic matching"""
    
    def __init__(self):
        try:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            logger.info("Sentence Transformer model loaded successfully")
        except HTTPException as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def get_embeddings(self, texts: List[str]) -> np.ndarray:
        """Generate embeddings for texts"""
        return self.model.encode(texts, convert_to_tensor=False)
    
    def semantic_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity between two texts"""
        embeddings = self.model.encode([text1, text2], convert_to_tensor=False)
        similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        return float(similarity)
    
    def match_skills(
        self,
        required_skills: List[str],
        candidate_skills: List[str]
    ) -> Dict:
        """Match skills between job and candidate"""
        required_set = set(skill.lower() for skill in required_skills)
        candidate_set = set(skill.lower() for skill in candidate_skills)
        
        matched = required_set.intersection(candidate_set)
        missing = required_set - candidate_set
        
        match_percentage = (len(matched) / len(required_set) * 100) if required_set else 0
        
        return {
            'matched_skills': list(matched),
            'missing_skills': list(missing),
            'match_percentage': match_percentage,
            'matched_count': len(matched),
            'required_count': len(required_set)
        }
    
    def calculate_match_score(
        self,
        semantic_score: float,
        skill_match: float,
        experience_match: bool,
        education_match: bool
    ) -> float:
        """Calculate weighted match score"""
        
        # Weights for different factors
        weights = {
            'semantic': 0.4,      # 40%
            'skills': 0.35,       # 35%
            'experience': 0.15,   # 15%
            'education': 0.10     # 10%
        }
        
        score = (
            semantic_score * weights['semantic'] * 100 +
            skill_match * weights['skills'] +
            (100 if experience_match else 0) * weights['experience'] +
            (100 if education_match else 0) * weights['education']
        )
        
        return min(100, max(0, score))
    
    def generate_recommendations(
        self,
        match_score: float,
        missing_skills: List[str],
        skill_gap: float
    ) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if match_score >= 85:
            recommendations.append("Excellent match! Consider scheduling an interview.")
        elif match_score >= 70:
            recommendations.append("Good match! The candidate has most required qualifications.")
        elif match_score >= 50:
            recommendations.append("Moderate match. Candidate may require training in specific areas.")
        else:
            recommendations.append("Low match. Consider reviewing other candidates.")
        
        if missing_skills:
            top_missing = missing_skills[:3]
            skills_text = ", ".join(top_missing)
            recommendations.append(f"Candidate lacks experience in: {skills_text}")
        
        if skill_gap > 0.3:
            recommendations.append("Consider providing technical training or mentoring.")
        
        return recommendations
