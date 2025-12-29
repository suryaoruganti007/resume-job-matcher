from sentence_transformers import SentenceTransformer
from fastapi import HTTPException
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class MLService:
    def __init__(self):
        try:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Model load failed: {str(e)}")
    
    def compute_similarity(self, resume_text: str, job_text: str) -> float:
        try:
            embeddings = self.model.encode([resume_text, job_text])
            similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
            return float(similarity * 100)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Similarity computation failed: {str(e)}")
