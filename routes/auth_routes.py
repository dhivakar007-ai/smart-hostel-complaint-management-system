from flask import Blueprint, render_template, request, redirect, url_for
from flask import session, flash

from models.student import Student
from models.admin import Admin

auth = Blueprint("auth", __name__)


# ---------------------------------------
# Login Page
# ---------------------------------------

@auth.route("/")
def home():

    if session.get("role") == "admin":
        return redirect(url_for("admin.dashboard"))

    if session.get("role") == "student":
        return redirect(url_for("student.dashboard"))

    return render_template("login.html")


# ---------------------------------------
# Login
# ---------------------------------------

@auth.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    admin = Admin.login(username, password)

    if admin:

        session.clear()

        session["id"] = admin["id"]
        session["username"] = admin["username"]
        session["role"] = "admin"

        flash("Welcome Administrator!", "success")

        return redirect(url_for("admin.dashboard"))

    student = Student.login(username, password)

    if student:

        session.clear()

        session["id"] = student["id"]
        session["username"] = student["username"]
        session["role"] = "student"

        flash("Login Successful.", "success")

        return redirect(url_for("student.dashboard"))

    flash("Invalid Username or Password.", "danger")

    return redirect(url_for("auth.home"))


# ---------------------------------------
# Student Registration
# ---------------------------------------

@auth.route("/register", methods=["POST"])
def register():

    try:

        Student.create(

            request.form["name"],

            request.form["email"],

            request.form["username"],

            request.form["password"],

            request.form.get("room_number", ""),

            request.form.get("phone", "")

        )

        flash("Registration Successful. Please login.", "success")

    except Exception:

        flash("Username or Email already exists.", "danger")

    return redirect(url_for("auth.home"))


# ---------------------------------------
# Logout
# ---------------------------------------

@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "info")

    return redirect(url_for("auth.home"))