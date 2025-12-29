from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class MLService:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    
    def compute_similarity(self, resume_text: str, job_text: str):
        # Fit on both texts
        texts = [resume_text, job_text]
        tfidf_matrix = self.vectorizer.fit_transform(texts)
        
        # Cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(similarity) * 100  # Convert to percentage
