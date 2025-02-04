import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["socialmedia"]

def save_page_data(data):
    db.pages.update_one({"page_url": data["page_url"]}, {"$set": data}, upsert=True)

def get_page_data(username):
    return db.pages.find_one({"page_url": f"https://www.facebook.com/{username}"})

def get_recent_posts(username, limit=10):
    return list(db.posts.find({"page_url": f"https://www.facebook.com/{username}"}).sort("created_at", -1).limit(limit))

def get_followers(username, limit=10, page=1):
    skip = (page - 1) * limit
    return list(db.followers.find({"page_url": f"https://www.facebook.com/{username}"}).skip(skip).limit(limit))

def filter_pages_by_followers(min_followers, max_followers):
    return list(db.pages.find({"total_followers": {"$gte": min_followers, "$lte": max_followers}}))

def filter_pages_by_name(name):
    return list(db.pages.find({"page_name": {"$regex": name, "$options": "i"}}))

def filter_pages_by_category(category):
    return list(db.pages.find({"page_category": {"$regex": category, "$options": "i"}}))