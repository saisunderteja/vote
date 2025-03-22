from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["vote_syss"]
polls_collection = db["polls"]
votes_collection = db["votes"]
