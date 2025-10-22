from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db import users_collection
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

# ----------------------------
# User model helpers
# ----------------------------
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def save_to_db(self, collection):
        collection.insert_one({
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "role": "user"
        })

    @staticmethod
    def find_by_username(collection, username):
        return collection.find_one({"username": username})

    @staticmethod
    def check_password(hashed_password, plain_password):
        return check_password_hash(hashed_password, plain_password)


# ----------------------------
# Routes
# ----------------------------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Please fill out both fields", "warning")
            return render_template("login.html")

        user = User.find_by_username(users_collection, username)

        if user is None:
            flash("User not found", "danger")
            return render_template("login.html")

        if not User.check_password(user.get("password", ""), password):
            flash("Invalid password", "danger")
            return render_template("login.html")

        # ✅ Login success
        session["user"] = username
        flash(f"Welcome, {username}!", "success")
        return redirect(url_for("dashboard.dashboard"))

    return render_template("login.html")



@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        if User.find_by_username(users_collection, username):
            flash("User already exists!", "warning")
        else:
            new_user = User(username, password, email)
            new_user.save_to_db(users_collection)
            flash("Registered successfully, please login.", "success")
            return redirect(url_for("auth.login"))
    return render_template("register.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))

