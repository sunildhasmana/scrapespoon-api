from flask import Blueprint, render_template, session, redirect, url_for
from db import users_collection

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    # Example: fetch extra info about logged-in user
    user = users_collection.find_one({"username": session["user"]})
    email = user.get("email", "Not provided")

    return render_template("dashboard.html", username=session["user"], email=email)

