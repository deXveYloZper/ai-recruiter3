from fastapi import FastAPI
from api.jobs import router as job_router
from api.candidates import router as candidate_router
# Import your OCR and NLP services (update with actual paths)
from services.ocr_service import perform_ocr
from services.nlp_service import extract_skills

app = FastAPI(title="AI Recruiter API")

# Include routers
app.include_router(job_router, prefix="/api/v1")
app.include_router(candidate_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Recruiter API"}

# Here you can add additional routes for OCR and NLP operations as required
# For example, an endpoint to perform OCR on an uploaded image
@app.post("/perform-ocr/")
async def ocr_endpoint(image_file: bytes = File(...)):
    text = perform_ocr(image_file)
    return {"extracted_text": text}

# Similarly, an endpoint for NLP tasks can be added
@app.post("/extract-skills/")
async def extract_skills_endpoint(text: str):
    skills = extract_skills(text)
    return {"skills": skills}
