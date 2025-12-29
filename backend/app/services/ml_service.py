def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    dot = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = sum(a * a for a in vec1) ** 0.5
    mag2 = sum(a * a for a in vec2) ** 0.5
    return dot / (mag1 * mag2) if mag1 and mag2 else 0.0

class MLService:
    def compute_similarity(self, resume_text: str, job_text: str) -> float:
        # Simple word overlap (bag-of-words)
        resume_words = set(resume_text.lower().split())
        job_words = set(job_text.lower().split())
        
        common = len(resume_words & job_words)
        total = len(resume_words | job_words)
        
        # Jaccard similarity as percentage
        score = (common / total * 100) if total > 0 else 0
        return float(max(0, min(100, score)))
