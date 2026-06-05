###################################################
# File: vote_schemas.py
# Description: Pydantic Data Models / Schemas
#--------------------------------------------------
# Purpose:
#   Defines the data structure and validation rules
#   for incoming API request bodies.
#
# How it works:
#   - PollSchema  : Validates poll creation data
#                   (question, options, duration)
#   - VoteSchema  : Validates vote submission data
#                   (voter details, aadhar, choice)
#   - Pydantic auto-validates all fields on request
###################################################
from pydantic import BaseModel
from datetime import datetime
from typing import List
from pydantic import field_validator
import re
class PollSchema(BaseModel):
    question: str
    options: List[str]
    duration: int  # Duration in seconds

class VoteSchema(BaseModel):
    poll_id: str
    first_name: str
    last_name: str
    phone_number: str
    aadhar_number: str
    choice: str


@field_validator("phone_number")
def validate_phone(cls, v):
    if not re.match(r"^[6-9]\d{9}$", v):  # Indian mobile format
        raise ValueError("Invalid Indian phone number")
    return v