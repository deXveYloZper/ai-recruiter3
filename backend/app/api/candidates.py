from fastapi import APIRouter

router = APIRouter()

@router.get("/candidates")
async def read_candidates():
    return {"message": "Returning all candidates"}
