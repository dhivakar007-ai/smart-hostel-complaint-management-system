from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from routes.auth_routes import login_required
from models.complaint import Complaint
from models.student import Student

student_bp = Blueprint("student", __name__, url_prefix="/student")


def student_required(view):
    return login_required(role="student")(view)


@student_bp.route("/dashboard")
@student_required
def dashboard():
    student_id = session["user_id"]
    complaints = Complaint.list_for_student(student_id)
    return render_template(
        "student/dashboard.html",
        complaints=complaints,
        name=session.get("name"),
    )


@student_bp.route("/submit-complaint", methods=["GET", "POST"])
@student_required
def submit_complaint():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        if not title or not description:
            flash("Title and description are required.", "warning")
            return render_template("student/submit_complaint.html")

        Complaint.create(session["user_id"], title, description)
        flash("Your complaint has been submitted.", "success")
        return redirect(url_for("student.complaint_history"))

    return render_template("student/submit_complaint.html")


@student_bp.route("/complaint-history")
@student_required
def complaint_history():
    student_id = session["user_id"]
    complaints = Complaint.list_for_student(student_id)
    return render_template(
        "student/complaint_history.html",
        complaints=complaints,
    )


@student_bp.route("/profile", methods=["GET", "POST"])
@student_required
def profile():
    student_id = session["user_id"]
    student = Student.get_by_id(student_id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        room_number = request.form.get("room_number", "").strip()

        if not name or not email:
            flash("Name and email cannot be blank.", "warning")
            return render_template("student/profile.html", student=student)

        Student.update_profile(student_id, name, email, room_number)
        flash("Profile updated successfully.", "success")
        return redirect(url_for("student.profile"))

    return render_template("student/profile.html", student=student)
