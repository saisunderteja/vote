from fastapi import FastAPI
from app.routes.poll_routes import router as poll_router
from app.routes.vote_routes import router as vote_router

app = FastAPI()

app.include_router(poll_router)
app.include_router(vote_router)


