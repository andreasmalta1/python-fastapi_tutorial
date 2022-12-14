from fastapi import FastAPI
from database import engine
from routers import post, user, auth, vote
from config import Settings
import models

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def home():
    return {"data": "home"}
