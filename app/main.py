###################################################
# File: main.py
# Description: Application Entry Point
#--------------------------------------------------
# Purpose:
#   Initializes the FastAPI application and
#   registers all route modules.
#
# How it works:
#   - Creates FastAPI app instance
#   - Includes poll_router for poll endpoints
#   - Includes vote_router for vote endpoints
#   - Run with: uvicorn app.main:app --reload --port xxxx
###################################################
from fastapi import FastAPI
from app.routes.poll_routes import router as poll_router
from app.routes.vote_routes import router as vote_router

app = FastAPI()

app.include_router(poll_router)
app.include_router(vote_router)


