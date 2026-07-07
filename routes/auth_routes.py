import sqlite3
from functools import wraps

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

from database.database import query_db
from models.admin import Admin
from models.student import Student

auth_bp = Blueprint("auth", __name__)


def login_required(role=None):
    def decorator(view):
        @wraps(view)
        def wrapped_view(*args, **kwargs):
            if "user_id" not in session:
                return redirect(url_for("auth.login"))
            if role and session.get("role") != role:
                flash("You do not have permission to access that page.", "warning")
                return redirect(url_for("auth.login"))
            return view(*args, **kwargs)

        return wrapped_view

    return decorator


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        user = query_db(
            "SELECT * FROM users WHERE username = ?;",
            (username,),
            one=True,
        )

        if not user:
            flash("Invalid username or password.", "danger")
            return render_template("login.html")

        if not check_password_hash(user["password"], password):
            flash("Invalid username or password.", "danger")
            return render_template("login.html")

        session.clear()
        session["user_id"] = user["id"]
        session["username"] = user["username"]
        session["role"] = user["role"]
        session["name"] = user["name"]

        if user["role"] == "admin":
            return redirect(url_for("admin.dashboard"))
        return redirect(url_for("student.dashboard"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        room_number = request.form.get("room_number", "").strip()

        if not username or not password or not name or not email:
            flash("All fields are required.", "warning")
            return render_template("login.html")

        try:
            Student.create(username, password, name, email, room_number)
            flash("Student registration successful. You may log in now.", "success")
            return redirect(url_for("auth.login"))
        except sqlite3.IntegrityError:
            flash("Username or email already exists.", "danger")

    return render_template("login.html")
