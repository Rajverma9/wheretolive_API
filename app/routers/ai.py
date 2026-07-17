from fastapi import APIRouter
router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/summary")
def ai_summary():
    return {"Message": "AI Summary"}

@router.get("/recommendation")
def ai_recommendation():
    return {"Message": "AI Recommendation"}