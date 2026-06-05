###################################################
# File: poll_routes.py
# Description: Poll API Route Definitions
#--------------------------------------------------
# Purpose:
#   Defines all HTTP endpoints related to poll
#   creation and management.
#
# How it works:
#   - POST /create_poll : Accepts poll data and
#                         delegates to poll_service
#   - Uses PollSchema for request body validation
#   - Returns poll_id on successful creation
###################################################
from fastapi import APIRouter
from app.models.vote_schemas import PollSchema
from app.services.poll_service import create_poll

router = APIRouter()

@router.post("/create_poll")
def create_poll_endpoint(data: PollSchema):
    return create_poll(data)
