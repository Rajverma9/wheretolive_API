from fastapi import APIRouter
router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/signup")
def signup():
    return {"Message": f"Signup Successfully"}

@router.post("/login")
def login():
    return {"Message": f"Login Successfully"}

@router.get("/profile")
def profile():
    return {"Message": f"Profile  Protected"} 