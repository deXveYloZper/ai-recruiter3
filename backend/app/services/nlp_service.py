# backend/app/nlp_service.py

import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    """Extract skills from text using SpaCy."""
    # Process the text
    doc = nlp(text)
    
    # Extract entities tagged as 'SKILL'
    skills = [entity.text for entity in doc.ents if entity.label_ == "SKILL"]
    
    return skills
