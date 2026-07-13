from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "WELCOME TO THE WHERE TO LIVE API 1.0"}