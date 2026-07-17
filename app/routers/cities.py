from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models.city import City, CityMetric

router = APIRouter(prefix="/cities", tags=["Cities"])

@router.get("/")
def list_cities(session: Session = Depends(get_session)) :
    return session.exec(select(City)).all()

@router.get("/{city_id}")
def list(city_id:int, session: Session = Depends(get_session)):
    city = session.get(City, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City Not Found")
    return city

@router.post("/")
def add_city():
    return {"Message": f"New City Created"}

@router.put("/{city_id}")
def update_city(city_id: int):
    return {"Message": f"City Id Updated{city_id}"}

@router.get("/{city_id}")
def history_city(city_id:int, session : Session= Depends(get_session)):
     statement = select(CityMetric).where(CityMetric.city_id == city_id)
     return session.exec(statement).all()