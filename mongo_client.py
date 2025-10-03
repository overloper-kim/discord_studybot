from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_CLI = os.environ.get("MONGO_CLI")

client = MongoClient(MONGO_CLI)
db = client["overloper_discord"]

if "users" in db.list_collection_names():
  user_col = db["users"]
  print(f"user_col:", user_col)
else:
  db.create_collection["users"]

if "menu" in db.list_collection_names():
  menu_col = db["menu"]
  print(f"menu_col:", menu_col)
else:
  db.create_collection["menu"]

if "study_time" in db.list_collection_names():
  study_col = db["study_time"]
  print(f"study_col:", study_col)
else:
  db.create_collection["study_time"]

if "timer" in db.list_collection_names():
  timer_col = db["timer"]
  print(f"timer:", timer_col)
else:
  db.create_collection["timer"]