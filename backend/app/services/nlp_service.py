import re

class NLPService:
    def extract_text_features(self, text: str) -> dict:
        # Extract skills, experience, education with regex
        skills = re.findall(r'\b[A-Za-z]{3,}\s*(?:Java|Python|React|FastAPI|Docker|AWS|Azure|SQL|MongoDB|Kubernetes)\b', text, re.I)
        experience = len(re.findall(r'\b(?:years?|yrs?)\s*(?:of)?\s*(?:experience|exp)\b', text, re.I))
        education = bool(re.findall(r'\b(?:B\.Tech|BE|BS|M\.Tech|MS|MSc|BSc|PhD)\b', text, re.I))
        
        return {
            "skills": list(set(skills))[:10],
            "experience_years": experience,
            "has_degree": education
        }
