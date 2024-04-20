from fastapi import File, FastAPI, UploadFile, HTTPException
from api.jobs import router as job_router
from api.candidates import router as candidate_router
from fastapi.responses import JSONResponse
# Import your OCR and NLP services (update with actual paths)
from services.ocr_service import perform_ocr
from services.nlp_service import extract_skills

import logging

# Initialize FastAPI app with a title
app = FastAPI(title="AI Recruiter API")

# Set up logging
logger = logging.getLogger("uvicorn.error")

# Include routers
# Include job and candidate routers with versioned API prefixes
app.include_router(job_router, prefix="/api/v1")
app.include_router(candidate_router, prefix="/api/v1")

@app.get("/")
async def root():
    """
    Root GET endpoint which returns a welcome message.
    """
    return {"message": "Welcome to the AI Recruiter API"}

# Here you can add additional routes for OCR and NLP operations as required
# For example, an endpoint to perform OCR on an uploaded image
@app.post("/perform-ocr/")
async def ocr_endpoint(file: UploadFile = File(...)):
    """
    POST endpoint to perform OCR on the uploaded image file.

    Args:
    file (UploadFile): An image file received as a part of the form data.

    Returns:
    JSONResponse: Contains the extracted text from the image.
    """
    try:
        # Read the image file as bytes, then perform OCR
        image_bytes = await file.read()
        extracted_text = await perform_ocr(image_bytes)
        return JSONResponse(content={"extracted_text": extracted_text}, status_code=200)
    except Exception as e:
        logger.error(f"OCR processing failed: {str(e)}")
        return JSONResponse(content={"error": "OCR processing failed", "details": str(e)}, status_code=500)


@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    """
    POST endpoint to extract text and skills from an uploaded image file.

    Args:
    file (UploadFile): An image file received as part of the form data.

    Returns:
    JSONResponse: Contains the extracted text and skills from the image.
    """
    try:
        image_bytes = await file.read()
        text = await perform_ocr(image_bytes)
        skills = await extract_skills(text)
        return JSONResponse(content={"text": text, "skills": skills}, status_code=200)
    except Exception as e:
        logger.error(f"Failed to extract text or skills: {str(e)}")
        return JSONResponse(content={"error": "Failed to process the image", "details": str(e)}, status_code=500)



@app.post("/extract-skills/")
async def extract_skills_endpoint(text: str):
    """
    POST endpoint to extract skills from a given text.

    Args:
    text (str): Text from which to extract skills.

    Returns:
    JSONResponse: Contains the skills extracted from the text.
    """
    try:
        skills = await extract_skills(text)
        return JSONResponse(content={"skills": skills}, status_code=200)
    except Exception as e:
        logger.error(f"Failed to extract skills: {str(e)}")
        return JSONResponse(content={"error": "Failed to analyze the text", "details": str(e)}, status_code=500)

