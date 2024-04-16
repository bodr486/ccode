from fastapi import FastAPI

from core.config import settings
from .auth.views import router as auth_router

app = FastAPI()
app.include_router(router=auth_router)

@app.get("/")
def hello():
    return{
        "message" : "Hello!",
    }