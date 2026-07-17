from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from sqlmodel import SQLModel
from app.database import engine
from app.routers import cities, auth, ranking, ai, comparisons
from app.middlewares.logging_middleware import log_requests

app = FastAPI()

#DB Connection
@app.on_event("startup")
def on_startup():
    try:
        SQLModel.metadata.create_all(engine)
        print("Database Connected Successfully")
    except OperationalError as e:
        print("Database Connection Failed" , e)


@app.get("/")
def home():
    return {"Message": "WELCOME TO THE WHERE TO LIVE API 1.0"}

app.include_router(cities.router)
app.include_router(auth.router)
app.include_router(ranking.router)
app.include_router(ai.router)
app.include_router(comparisons.router)
app.middleware("http")(log_requests)