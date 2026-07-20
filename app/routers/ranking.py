from fastapi import APIRouter,  Depends
from sqlmodel import Session
from app.database import get_session
from app.services.ranking_service import get_overall_ratings

router = APIRouter(prefix="/ranking", tags= ["Ranking"])

@router.get("/")
def overall_ranking(session: Session = Depends(get_session)):
    return get_overall_ratings(session)

@router.get("/state/{state}")
def state_ranking(state:str):
    return {"Message": f"State Ranking{state}"}

@router.get("/compares")
def compare_cities(city1: str, city2:str):
    return {"Message": f"{city1} vs {city2}"}