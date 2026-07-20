from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from app.database import get_session
from app.models.user import User
from app.services.auth_service import hash_password, verify_password, create_access_token
from app.services.dependencies import get_current_user

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
def login(form_data: OAuth2PasswordRequestForm= Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token , "token_type": "bearer"}

@router.get("/profile")
def profile(current_user: User = Depends(get_current_user)):
    return {"name": current_user.name, "email": current_user.email}
