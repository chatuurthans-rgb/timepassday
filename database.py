from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://jobhub:abhy1728@cluster0.ud2aekq.mongodb.net/"
)

db = client["jobhub"]

user_collection = db["users"]
jobs_collection = db["jobs"]
applications_collection = db["applications"]
