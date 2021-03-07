"""
Author: Muhammad Omer Khalil
"""
import os
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

class MongoSettings():
    uri: str =  os.getenv("MONGO_ATLAS_CONNECTION_STRING") # replace credentials with .env variables
    database: str = "todolist"
    collection: str = "todolist_resources"

mongo_settings = MongoSettings()

client = MongoClient(mongo_settings.uri)
_db: Database = client[mongo_settings.database]