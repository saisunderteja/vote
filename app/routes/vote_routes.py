from fastapi import APIRouter
from app.models.vote_schemas import VoteSchema
from app.services.vote_service import cast_vote, count_valid_votes, pick_random_winner

router = APIRouter()

@router.post("/vote")
def vote_endpoint(data: VoteSchema):
    return cast_vote(data)

@router.get("/count_votes/{poll_id}")
def count_votes_endpoint(poll_id: str):
    return count_valid_votes(poll_id)


@router.get("/winner/{poll_id}")
def winner_endpoint(poll_id: str):
    return pick_random_winner(poll_id)