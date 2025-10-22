from pymongo import MongoClient, errors
from werkzeug.security import generate_password_hash

# ----------------------------
# MongoDB server admin credentials
# ----------------------------
# Use the root/admin credentials for the server
ROOT_USER = "root"        # your MongoDB root username
ROOT_PASSWORD = "rootpass"  # your MongoDB root password
MONGO_HOST = "localhost"
MONGO_PORT = 27017

# ----------------------------
# Application database & user
# ----------------------------
DB_NAME = "scrapespoon_db"
APP_MONGO_USER = "admin"
APP_MONGO_PASSWORD = "StrongPassword123"

# ----------------------------
# First Flask admin user
# ----------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Admin123!"  # change to a strong password
ADMIN_EMAIL = "admin@example.com"

# ----------------------------
# Connect to MongoDB as root
# ----------------------------
try:
    client = MongoClient(f"mongodb://{ROOT_USER}:{ROOT_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/")
    db = client[DB_NAME]
    print(f"Connected to MongoDB server at {MONGO_HOST}:{MONGO_PORT}")
except errors.ConnectionFailure as e:
    print("Failed to connect to MongoDB:", e)
    exit(1)

# ----------------------------
# Create application MongoDB user
# ----------------------------
try:
    db.command("createUser", APP_MONGO_USER,
               pwd=APP_MONGO_PASSWORD,
               roles=[{"role": "readWrite", "db": DB_NAME}])
    print(f"MongoDB user '{APP_MONGO_USER}' created successfully for database '{DB_NAME}'")
except errors.OperationFailure as e:
    if "already exists" in str(e):
        print(f"MongoDB user '{APP_MONGO_USER}' already exists.")
    else:
        print("Error creating MongoDB user:", e)
        exit(1)

# ----------------------------
# Insert first Flask admin user
# ----------------------------
users_collection = db["users"]

hashed_password = generate_password_hash(ADMIN_PASSWORD)

if users_collection.find_one({"username": ADMIN_USERNAME}):
    print(f"Flask admin user '{ADMIN_USERNAME}' already exists.")
else:
    users_collection.insert_one({
        "username": ADMIN_USERNAME,
        "password": hashed_password,
        "email": ADMIN_EMAIL,
        "role": "admin"
    })
    print(f"Flask admin user '{ADMIN_USERNAME}' created successfully!")

