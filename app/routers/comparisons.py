from fastapi import APIRouter
router = APIRouter(prefix="/comparisons", tags=["Comparison"])

@router.post("/")
def save_comparison():
    return {"Message": "Save Comparison"}

@router.get("/mine")
def my_comparison():
    return {"Message": "My Saved Comparisons"} 