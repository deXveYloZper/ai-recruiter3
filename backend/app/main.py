from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import logging

# Local imports for modular services
from api.jobs import router as job_router
from api.candidates import router as candidate_router
from services.ocr_service import perform_ocr
from services.skills_extraction_service import extract_direct_skills, infer_skills
from services.experience_service import extract_experience_details
from services.career_progression_service import analyze_career_progression
from services.company_profiles_service import fetch_company_profile

# Initialize the FastAPI application with metadata
app = FastAPI(title="AI Recruiter API")

# Configure logging
logger = logging.getLogger("uvicorn.error")

# Register API routes from other modules
app.include_router(job_router, prefix="/api/v1/jobs")
app.include_router(candidate_router, prefix="/api/v1/candidates")

@app.get("/")
async def root():
    """
    Root GET endpoint which returns a welcome message.
    """
    return {"message": "Welcome to the AI Recruiter API"}

class TextExtractionRequest(BaseModel):
    text: str

@app.post("/perform-ocr/")
async def ocr_endpoint(file: UploadFile = File(...)):
    """
    Endpoint to perform OCR on an uploaded image file and extract text.
    """
    try:
        image_bytes = await file.read()
        extracted_text = await perform_ocr(image_bytes)
        return JSONResponse(content={"extracted_text": extracted_text}, status_code=200)
    except Exception as e:
        logger.error(f"OCR processing failed: {e}")
        return JSONResponse(content={"error": "OCR processing failed", "details": str(e)}, status_code=500)

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    """
    Endpoint to extract text and skills from an uploaded image file.
    """
    try:
        image_bytes = await file.read()
        text = await perform_ocr(image_bytes)
        skills = extract_direct_skills(text)
        return JSONResponse(content={"text": text, "skills": skills}, status_code=200)
    except Exception as e:
        logger.error(f"Failed to extract text or skills: {e}")
        return JSONResponse(content={"error": "Failed to process the image", "details": str(e)}, status_code=500)

@app.post("/extract-skills/")
async def extract_skills_endpoint(request: TextExtractionRequest):
    """
    Endpoint to extract skills from provided text using NLP techniques.
    """
    try:
        skills = extract_direct_skills(request.text)
        return JSONResponse(content={"skills": skills}, status_code=200)
    except ValidationError as ve:
        return JSONResponse(content={"error": "Invalid input", "details": str(ve)}, status_code=400)
    except Exception as e:
        logger.error(f"Failed to extract skills: {e}")
        return JSONResponse(content={"error": "Failed to analyze the text", "details": str(e)}, status_code=500)
    
@app.post("/analyze-cv/")
async def analyze_cv(cv_text: str):
    """
    Comprehensive CV analysis endpoint to extract skills, experience, and career progression.
    """
    try:
        skills = extract_direct_skills(cv_text)
        inferred_skills = infer_skills("Software Engineer", "Tech")
        experience_details = extract_experience_details(cv_text)
        career_progress = analyze_career_progression(experience_details['roles'])
        company_profile = fetch_company_profile("OpenAI")
        return JSONResponse(content={
            "skills": skills + inferred_skills,
            "experience": experience_details,
            "career_progression": career_progress,
            "company_profile": company_profile
        }, status_code=200)
    except Exception as e:
        logger.error(f"CV analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Additional endpoint examples can be added here with similar structure
