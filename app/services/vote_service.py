###################################################
# File: vote_service.py
# Description: Vote Business Logic
#--------------------------------------------------
# Purpose:
#   Contains all core business logic for casting
#   votes, counting results, and declaring winner.
#
# How it works:
#   - cast_vote()
#       * Validates Aadhaar number format
#       * Checks poll exists and is still active
#       * Validates voter's choice against options
#       * Prevents duplicate voting per Aadhaar
#       * Saves vote record to MongoDB
#
#   - count_valid_votes()
#       * Fetches all votes within poll time window
#       * Groups and counts votes per option
#       * Returns result breakdown per option
#
#   - get_poll_winner()
#       * Counts votes per option
#       * Finds option with highest vote count
#       * Handles tie cases
#       * Returns winner with full result summary
###################################################
from app.db.vote_db import votes_collection, polls_collection
from datetime import datetime
from bson import ObjectId
from collections import defaultdict
import random
from fastapi import HTTPException


# -------------------------------
# Aadhaar Validation (basic + mock)
# -------------------------------
def validate_aadhar(aadhar_number: str):
    # Check length and numeric
    if len(aadhar_number) != 12 or not aadhar_number.isdigit():
        return False


    if aadhar_number == "000000000000":  # reject all-zeros
        return False
    first_digit = int(aadhar_number[0])
    return first_digit in range(1, 10)  # no leading zero

def cast_vote(data):
    # Aadhaar validation
    if not validate_aadhar(data.aadhar_number):
        raise HTTPException(status_code=400, detail="Invalid Aadhaar number")

    # Check poll exists
    poll = polls_collection.find_one({"_id": ObjectId(data.poll_id)})
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")

    current_time = datetime.utcnow()

    # Check voting window
    if not (poll["start_time"] <= current_time <= poll["end_time"]):
        return {"error": "Voting is closed for this poll"}

    # NEW: Validate choice
    valid_options = poll.get("options", [])
    normalized_options = [opt.lower() for opt in valid_options]

    if data.choice.lower() not in normalized_options:
        return {
            "error": f"Invalid choice. Allowed options are: {valid_options}"
        }

    # Prevent duplicate voting
    existing_vote = votes_collection.find_one({
        "poll_id": data.poll_id,
        "aadhar_number": data.aadhar_number
    })

    if existing_vote:
        return {"error": "You have already voted in this poll"}

    # Save vote
    vote = {
        "poll_id": data.poll_id,
        "first_name": data.first_name,
        "last_name": data.last_name,
        "phone_number": data.phone_number,
        "aadhar_number": data.aadhar_number,
        "choice": data.choice,
        "timestamp": current_time
    }




    votes_collection.insert_one(vote)

    return {"message": "Vote cast successfully"}

# -------------------------------
# Count Valid Votes
# -------------------------------
def count_valid_votes(poll_id):
    poll = polls_collection.find_one({"_id": ObjectId(poll_id)})
    if not poll:
        return {"error": "Poll not found"}

    valid_votes = votes_collection.find({
        "poll_id": poll_id,
        "timestamp": {
            "$gte": poll["start_time"],
            "$lte": poll["end_time"]
        }
    })

    vote_count = defaultdict(int)

    for vote in valid_votes:
        vote_count[vote["choice"]] += 1  

    return {
        "poll_id": poll_id,
        "results": dict(vote_count)
    }





def get_poll_winner(poll_id):
    poll = polls_collection.find_one({"_id": ObjectId(poll_id)})
    if not poll:
        return {"error": "Poll not found"}

    # Get all valid votes within poll time window
    valid_votes = list(votes_collection.find({
        "poll_id": poll_id,
        "timestamp": {
            "$gte": poll["start_time"],
            "$lte": poll["end_time"]
        }
    }))

    if not valid_votes:
        return {"message": "No valid votes for this poll"}

    # Count votes per option
    vote_count = defaultdict(int)
    for vote in valid_votes:
        vote_count[vote["choice"]] += 1

    # Find the winning option (highest votes)
    winning_option = max(vote_count, key=lambda k: vote_count[k])
    highest_votes = vote_count[winning_option]

    # Check for a tie
    tied_options = [opt for opt, count in vote_count.items() if count == highest_votes]

    if len(tied_options) > 1:
        return {
            "message": "It's a tie!",
            "tied_options": tied_options,
            "votes": highest_votes,
            "all_results": dict(vote_count)
        }

    return {
        "message": "Winner announced!",
        "winning_option": winning_option,
        "votes": highest_votes,
        "total_votes": len(valid_votes),
        "all_results": dict(vote_count)
    }
