from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_CLI = os.environ.get("MONGO_CLI")

client = MongoClient(MONGO_CLI)

db = client['sample_mflix']

print(db)