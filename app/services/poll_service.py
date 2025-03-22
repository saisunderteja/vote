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
