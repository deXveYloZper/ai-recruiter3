import spacy
from typing import List

# Load the SpaCy model for natural language processing
nlp = spacy.load("en_core_web_sm")

def extract_direct_skills(text: str) -> List[str]:
    """
    Extracts direct skills listed in the CV text using SpaCy's named entity recognition.

    Args:
    text (str): The text content of a CV from which to extract skills directly mentioned.

    Returns:
    List[str]: A list of skills explicitly mentioned in the text.
    """
    doc = nlp(text)
    # Extract entities that are tagged as 'SKILL' by the NLP model
    return [ent.text for ent in doc.ents if ent.label_ == "SKILL"]

def infer_skills(job_title: str, industry: str) -> List[str]:
    """
    Infers skills based on job roles and industry context, utilizing predefined mappings.

    Args:
    job_title (str): The job title from which to infer related skills.
    industry (str): The industry context to adjust skill inference accordingly.

    Returns:
    List[str]: A list of inferred skills based on the job title and industry context.
    """
    inferred_skills = []
    # Example condition to infer skills based on job title and industry
    if "software engineer" in job_title.lower():
        if "tech" in industry.lower():
            inferred_skills.extend(["scalable architectures", "cloud deployment"])
        elif "finance" in industry.lower():
            inferred_skills.extend(["high-frequency trading", "data security"])
    # Additional conditions can be added here for other job titles and industries
    return inferred_skills
