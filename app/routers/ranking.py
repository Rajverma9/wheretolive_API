from fastapi import APIRouter
router = APIRouter(prefix="/ranking", tags= ["Ranking"])

@router.get("/")
def overall_ranking():
    return {"Message": f"Overall Ranking"}

@router.get("/state/{state}")
def state_ranking(state:str):
    return {"Message": f"State Ranking{state}"}

@router.get("/compares")
def compare_cities(city1: str, city2:str):
    return {"Message": f"{city1} vs {city2}"}