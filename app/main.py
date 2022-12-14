from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from app.routers import post, user, auth, vote
except ImportError as e:
    from routers import post, user, auth, vote

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def home():
    return {"data": "home"}
