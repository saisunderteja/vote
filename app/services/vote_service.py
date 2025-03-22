from app.db.vote_db import votes_collection, polls_collection
from datetime import datetime
from bson import ObjectId

def cast_vote(data):
    poll = polls_collection.find_one({"_id": ObjectId(data.poll_id)})
    if not poll:
        return {"error": "Invalid poll ID"}
    
    current_time = datetime.utcnow()
    
    if not (poll["start_time"] <= current_time <= poll["end_time"]):
        return {"error": "Voting is closed for this poll"}
    
    vote = {
        "poll_id": data.poll_id,
        "first_name": data.first_name,
        "last_name": data.last_name,
        "phone_number": data.phone_number,
        "choice": data.choice,
        "timestamp": current_time
    }
    
    votes_collection.insert_one(vote)
    return {"message": "Vote cast successfully"}

from collections import defaultdict

def count_valid_votes(poll_id):
    poll = polls_collection.find_one({"_id": ObjectId(poll_id)})
    if not poll:
        return {"error": "Poll not found"}

    valid_votes = votes_collection.find({
        "poll_id": poll_id,
        "timestamp": {"$gte": poll["start_time"], "$lte": poll["end_time"]}
    })

    vote_count = defaultdict(int)
    
    for vote in valid_votes:
        vote_count[vote["choice"]] += 1

    return {"poll_id": poll_id, "results": dict(vote_count)}




import random

def pick_random_winner(poll_id):
    poll = polls_collection.find_one({"_id": ObjectId(poll_id)})
    if not poll:
        return {"error": "Poll not found"}

    valid_voters = list(votes_collection.find({
        "poll_id": poll_id,
        "timestamp": {"$gte": poll["start_time"], "$lte": poll["end_time"]}
    }))

    if not valid_voters:
        return {"message": "No valid votes for this poll"}

    winner = random.choice(valid_voters)
    return {
        "message": "Winner announced!",
        "first_name": winner["first_name"],
        "last_name": winner["last_name"],
        "phone_number": winner["phone_number"]
    }

