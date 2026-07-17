from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models.user import User
from app.services.auth_service import hash_password

router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/signup")
def signup(name:str, email:str, password:str, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.email == email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(name=name, email=email, password=hash_password(password))
    session.add(user)
    session.commit()
    return {"Message": f"Signup Successfully"}

@router.post("/login")
def login():
    return {"Message": f"Login Successfully"}

@router.get("/profile")
def profile():
    return {"Message": f"Profile  Protected"}