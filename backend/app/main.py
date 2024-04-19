from fastapi import FastAPI
from api.jobs import router as job_router
from api.candidates import router as candidate_router

app = FastAPI(title="AI Recruiter API")

# Include routers
app.include_router(job_router, prefix="/api/v1")
app.include_router(candidate_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Recruiter API"}
