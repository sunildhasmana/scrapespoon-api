from pymongo import MongoClient

client = MongoClient("mongodb://admin:StrongPassword123@localhost:27017/scrapespoon_db")
db = client["scrapespoon_db"]
users = db["users"].find()
for u in users:
    print(u)

