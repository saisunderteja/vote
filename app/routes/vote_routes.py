###################################################
# File: vote_routes.py
# Description: Vote API Route Definitions
#--------------------------------------------------
# Purpose:
#   Defines all HTTP endpoints related to voting,
#   vote counting, and winner declaration.
#
# How it works:
#   - POST /vote                  : Cast a vote
#   - GET  /count_votes/{poll_id} : Get vote counts
#   - GET  /winner/{poll_id}      : Get poll winner
#   - Delegates logic to vote_service
###################################################
from fastapi import APIRouter
from app.models.vote_schemas import VoteSchema
from app.services.vote_service import cast_vote, count_valid_votes, get_poll_winner

router = APIRouter()

@router.post("/vote")
def vote_endpoint(data: VoteSchema):
    return cast_vote(data)

@router.get("/count_votes/{poll_id}")
def count_votes_endpoint(poll_id: str):
    return count_valid_votes(poll_id)


@router.get("/winner/{poll_id}")
def winner_endpoint(poll_id: str):
    return get_poll_winner(poll_id)
