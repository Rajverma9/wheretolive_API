from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models.city import City, CityMetric
from app.services.llm_service import(generate_comparison_summary, generate_recommendation)

router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/summary")
async def ai_summary(city1: str, city2: str, session: Session= Depends(get_session)):
    c1 = session.exec(select(City).where(City.name == city1)).first()
    c2 = session.exec(select(City).where(City.name == city2)).first()
    if not c1 or not c2:
        raise HTTPException(status_code=404, detail="City Not Found")
    try:
        summary = await generate_comparison_summary(c1.dict(), c2.dict())
        return {"Summary": summary}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"AI Service failed:{e}")
    
@router.get("/recommendation")
def ai_recommendation():
    return {"Message": "AI Recommendation"}