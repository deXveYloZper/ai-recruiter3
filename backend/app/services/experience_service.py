import re

def extract_experience_details(text: str) -> dict:
    """
    Extract job roles, duration, and key responsibilities from CV text using regex as a placeholder.
    
    Args:
    text (str): The text content of a CV from which to extract experience details.
    
    Returns:
    dict: A dictionary with roles, durations, and responsibilities extracted from the CV.
    """
    # Example function to extract roles, duration, and responsibilities
    # Note: In a real-world application, replace regex with NLP processing.
    roles = re.findall(r"\b(?:Senior Developer|Project Manager|Software Engineer)\b", text)
    durations = re.findall(r"\b\d{4}-\d{4}\b", text)
    responsibilities = re.findall(r"(?<=responsible for ).*?(?=\.|\,)", text, flags=re.I)

    return {
        "roles": roles,
        "durations": durations,
        "responsibilities": responsibilities
    }

# Example usage
cv_text = """
    John Doe has worked as a Senior Developer from 2015-2020, responsible for leading the development team. 
    Then, he moved to the role of Project Manager from 2020-2022, responsible for managing project delivery and timelines.
"""

# Call the function to see the output
extracted_details = extract_experience_details(cv_text)
print(extracted_details)
