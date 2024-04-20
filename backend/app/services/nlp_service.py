# backend/app/nlp_service.py

import spacy
import asyncio

nlp = spacy.load("en_core_web_sm")

async def extract_skills(text):
    """Extract skills asynchronously from text using SpaCy."""
    loop = asyncio.get_event_loop()

    # Process the text using executor to avoid blocking the event loop on CPU-bound task
    doc = await loop.run_in_executor(None, nlp, text)
    
    # Extract entities tagged as 'SKILL'
    skills = [entity.text for entity in doc.ents if entity.label_ == "SKILL"]
    
    return skills
