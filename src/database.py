import os
from pymongo import MongoClient


CONNECTION_URL = os.getenv("CONNECTION_URL")
cluster = MongoClient(CONNECTION_URL)
db = cluster["PHYS122"]