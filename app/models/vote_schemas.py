from pydantic import BaseModel
from datetime import datetime
from typing import List

class PollSchema(BaseModel):
    question: str
    options: List[str]
    duration: int  # Duration in seconds

class VoteSchema(BaseModel):
    poll_id: str
    first_name: str
    last_name: str
    phone_number: str
    choice: str
