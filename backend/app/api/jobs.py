from fastapi import APIRouter

router = APIRouter()

@router.get("/jobs")
async def read_jobs():
    return {"message": "Returning all job postings"}
