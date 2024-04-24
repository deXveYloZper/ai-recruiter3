import spacy
import asyncio
from typing import List

# Load the pre-trained SpaCy model
nlp = spacy.load("en_core_web_sm")

async def extract_skills(text: str) -> List[str]:
    """
    Asynchronously extract skills from text using SpaCy. This function identifies entities
    that have been tagged as 'SKILL' by the NLP model.
    
    Args:
    text (str): The input text from which skills need to be extracted.

    Returns:
    List[str]: A list of skills extracted from the text.
    """
    loop = asyncio.get_event_loop()

    # Use an executor to perform the NLP parsing to avoid blocking the async loop
    # This is necessary as SpaCy's processing is synchronous and CPU-bound
    doc = await loop.run_in_executor(None, lambda: nlp(text))
    
    # Extract entities tagged as 'SKILL' and return them as a list of strings
    skills = [entity.text for entity in doc.ents if entity.label_ == "SKILL"]
    
    return skills

async def extract_comprehensive_skills(text: str, context: dict) -> List[str]:
    """
    Extract skills from the text considering additional context such as job titles
    and industries which helps in inferring implicit skills not directly mentioned in the text.

    Args:
    text (str): The input text from which to extract skills.
    context (dict): A dictionary containing additional information like job title and industry
                    to aid in skill inference.

    Returns:
    List[str]: A list of both explicitly mentioned and inferred skills.
    """
    skills = await extract_skills(text)
    inferred_skills = infer_skills_based_on_context(context)
    return skills + inferred_skills

def infer_skills_based_on_context(context: dict) -> List[str]:
    """
    Infer additional skills based on the provided context such as job title and industry.
    
    Args:
    context (dict): Context information including job title and industry.

    Returns:
    List[str]: A list of inferred skills based on the job role and industry context.
    """
    inferred_skills = []
    if "software engineer" in context.get("job_title", "").lower() and "tech" in context.get("industry", "").lower():
        inferred_skills.extend(["scalable architectures", "cloud deployment", "system design"])
    # Extend with more conditions as needed for other roles and industries
    return inferred_skills
