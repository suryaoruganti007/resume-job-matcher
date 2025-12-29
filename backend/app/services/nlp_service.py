import spacy
from typing import List, Set, Dict, Tuple
import re
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class NLPService:
    """NLP processing for resume and job descriptions"""
    
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
            logger.info("SpaCy model loaded successfully")
        except OSError:
            logger.error("SpaCy model not found. Running: python -m spacy download en_core_web_sm")
            raise
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep important ones
        text = re.sub(r'[^\w\s\-\.]', ' ', text)
        
        return text.strip()
    
    def extract_skills(self, text: str) -> Set[str]:
        """Extract technical skills from text"""
        # Common technical skills list
        common_skills = {
            'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'go', 'rust',
            'react', 'angular', 'vue', 'nodejs', 'express', 'fastapi', 'django',
            'sql', 'mongodb', 'postgresql', 'mysql', 'redis', 'elasticsearch',
            'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'git', 'jenkins',
            'machine learning', 'deep learning', 'nlp', 'computer vision', 'tensorflow',
            'pytorch', 'scikit-learn', 'pandas', 'numpy', 'spacy', 'html', 'css',
            'rest', 'graphql', 'microservices', 'agile', 'scrum', 'devops'
        }
        
        cleaned_text = self.clean_text(text)
        tokens = cleaned_text.split()
        
        found_skills = set()
        for skill in common_skills:
            if skill in cleaned_text:
                found_skills.add(skill)
        
        return found_skills
    
    def extract_experience_years(self, text: str) -> Tuple[int, int]:
        """Extract experience years from text"""
        # Pattern matching for years of experience
        patterns = [
            r'(\d+)\s*(?:\+)?\s*years?',
            r'(\d+)\s*(?:to|-)\s*(\d+)\s*years?'
        ]
        
        years_found = []
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                if len(match.groups()) == 2:
                    try:
                        years_found.append(int(match.group(2)) - int(match.group(1)))
                    except:
                        pass
                else:
                    try:
                        years_found.append(int(match.group(1)))
                    except:
                        pass
        
        if years_found:
            return min(years_found), max(years_found)
        return 0, 0
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract named entities using spaCy"""
        doc = self.nlp(text[:1000000])  # Limit text size for processing
        
        entities = {
            'ORG': [],
            'PERSON': [],
            'GPE': [],
            'PRODUCT': []
        }
        
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent.text)
        
        return entities
    
    def tokenize(self, text: str) -> List[str]:
        """Tokenize text"""
        doc = self.nlp(text[:500000])
        return [token.text for token in doc if not token.is_stop]
    
    def process_document(self, text: str, doc_type: str = "resume") -> Dict:
        """Complete document processing"""
        cleaned_text = self.clean_text(text)
        
        return {
            'original_text': text,
            'cleaned_text': cleaned_text,
            'skills': list(self.extract_skills(text)),
            'entities': self.extract_entities(text),
            'tokens': self.tokenize(text),
            'experience_years': self.extract_experience_years(text),
            'document_type': doc_type,
            'processed_at': datetime.now().isoformat()
        }
