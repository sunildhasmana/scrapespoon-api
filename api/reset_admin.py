from pymongo import MongoClient
from werkzeug.security import generate_password_hash

MONGO_URI = "mongodb://admin:StrongPassword123@localhost:27017/scrapespoon_db"
client = MongoClient(MONGO_URI)
db = client["scrapespoon_db"]
users = db["users"]

# Clear old admin (if any)
users.delete_many({"username": "admin"})

# Insert fresh admin with hashed password
admin_user = {
    "username": "admin",
    "password": generate_password_hash("Admin123!"),  # hashed securely
    "email": "admin@example.com",
    "role": "admin"
}
users.insert_one(admin_user)

print("✅ Admin user inserted successfully:")
print(f"   Username: admin")
print(f"   Password: Admin123! (hashed in DB)")

