from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page or dashboard redirect
@app.route("/")
def home():
    return redirect(url_for("login"))

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # Add login logic here
        return "Logged in"
    return render_template("login.html")

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Add registration logic here
        return "Registered"
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
