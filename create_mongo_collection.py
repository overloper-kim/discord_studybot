from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_CLI = os.environ.get("MONGO_CLI")

client = MongoClient(MONGO_CLI)
db = client["overloper_discord"]

'''
현재 discrod 봇에 필요한 collection 생성
'''
db.create_collection("users")
db.create_collection("menu")
db.create_collection("study_time")
db.create_collection("timer")