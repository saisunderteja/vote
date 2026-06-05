###################################################
# File: vote_db.py
# Description: Database Collections Configuration
#--------------------------------------------------
# Purpose:
#   Defines and exposes MongoDB collections used
#   across the application.
#
# How it works:
#   - Loads MongoDB URI from environment variables
#   - Connects to 'vote_sys' database
#   - Exposes 'polls' collection for poll data
#   - Exposes 'votes' collection for vote records
###################################################
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["vote_syss"]
polls_collection = db["polls"]
votes_collection = db["votes"]
