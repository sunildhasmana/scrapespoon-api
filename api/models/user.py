from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password, email, role="user"):
        self.username = username
        # Always store password as a hash
        self.password = generate_password_hash(password)
        self.email = email
        self.role = role

    def save_to_db(self, users_collection):
        user_data = {
            "username": self.username,
            "password": self.password,  # hashed password
            "email": self.email,
            "role": self.role,
        }
        users_collection.insert_one(user_data)

    @staticmethod
    def find_by_username(users_collection, username):
        return users_collection.find_one({"username": username})

    @staticmethod
    def check_password(stored_password_hash, provided_password):
        # Compare provided password with stored hash
        return check_password_hash(stored_password_hash, provided_password)

