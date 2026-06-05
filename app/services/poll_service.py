###################################################
# File: poll_service.py
# Description: Poll Business Logic
#--------------------------------------------------
# Purpose:
#   Contains all business logic related to poll
#   creation and management.
#
# How it works:
#   - Accepts poll data from poll_routes
#   - Calculates start_time and end_time based
#     on duration provided (in seconds)
#   - Inserts poll document into MongoDB
#   - Returns generated poll_id to the caller
###################################################
from app.db.vote_db import polls_collection
from datetime import datetime, timedelta

def create_poll(data):
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(seconds=data.duration)
    
    poll = {
        "question": data.question,
        "options": data.options,
        "start_time": start_time,
        "end_time": end_time
    }
    
    poll_id = polls_collection.insert_one(poll).inserted_id
    return {"poll_id": str(poll_id)}
