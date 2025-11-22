from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "transflow")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "corridas")

client = MongoClient(MONGO_URL)
db = client[MONGO_DB]
corridas_collection = db[MONGO_COLLECTION]
