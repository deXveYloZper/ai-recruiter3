# app/services/career_progression_service.py

from typing import List

def analyze_career_progression(experiences: List[dict]) -> dict:
    """
    Analyzes career progression from a list of job experiences.
    
    Args:
    experiences (List[dict]): A list of dictionaries where each dictionary contains information
    about a job experience, including the role and the industry.

    Returns:
    dict: A dictionary containing counts of promotions and transitions based on the provided experiences.
    """
    progression = {
        "promotions": 0,
        "transitions": 0
    }
    previous_role_level = 0
    previous_industry = None if not experiences else experiences[0]['industry']

    for experience in experiences:
        current_role_level = determine_role_level(experience['role'])
        current_industry = experience['industry']

        # Count promotion if current role level is higher than the previous one
        if current_role_level > previous_role_level:
            progression["promotions"] += 1

        # Count transition if the current industry differs from the previous one
        if current_industry != previous_industry:
            progression["transitions"] += 1

        # Update for next iteration
        previous_role_level = current_role_level
        previous_industry = current_industry

    return progression

def determine_role_level(role: str) -> int:
    """
    Determines the level of a job role for progression analysis based on predefined role levels.
    
    Args:
    role (str): The job role title as a string.

    Returns:
    int: Numeric representation of the role level, higher numbers indicate higher responsibility roles.
    """
    role = role.lower()
    if "manager" in role:
        return 2
    elif "senior" in role:
        return 1
    else:
        return 0

