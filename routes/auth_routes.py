from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from database.db import db

auth = Blueprint("auth", __name__)


# ==========================================
# Register
# ==========================================

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        role = request.form["role"]

        # Check if email already exists
        user = db.fetch_one(
            "SELECT id FROM users WHERE email=%s",
            (email,)
        )

        if user:
            flash("Email already registered.", "danger")
            return redirect(url_for("auth.register"))

        # Hash password
        hashed_password = generate_password_hash(password)

        # Save user
        db.execute(
            """
            INSERT INTO users(fullname, email, password, role)
            VALUES(%s, %s, %s, %s)
            """,
            (fullname, email, hashed_password, role)
        )

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# ==========================================
# Login
# ==========================================

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        user = db.fetch_one(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["fullname"] = user["fullname"]
            session["role"] = user["role"]

            flash("Login successful.", "success")

            if user["role"] == "recruiter":
                return redirect("/recruiter/dashboard")

            return redirect("/candidate/dashboard")

        flash("Invalid email or password.", "danger")

    return render_template("login.html")


# ==========================================
# Logout
# ==========================================

@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "info")

    return redirect(url_for("auth.login"))