from fastapi import APIRouter
from app.models.vote_schemas import PollSchema
from app.services.poll_service import create_poll

router = APIRouter()

@router.post("/create_poll")
def create_poll_endpoint(data: PollSchema):
    return create_poll(data)
