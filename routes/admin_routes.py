import sqlite3

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from routes.auth_routes import login_required
from models.admin import Admin
from models.complaint import Complaint
from models.student import Student

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


def admin_required(view):
    return login_required(role="admin")(view)


@admin_bp.route("/dashboard")
@admin_required
def dashboard():
    stats = Admin.get_statistics()
    return render_template("admin/dashboard.html", stats=stats)


@admin_bp.route("/complaints", methods=["GET", "POST"])
@admin_required
def complaints():
    if request.method == "POST":
        complaint_id = request.form.get("complaint_id")
        status = request.form.get("status")
        admin_note = request.form.get("admin_note", "").strip()

        if complaint_id and status:
            Complaint.update_status(complaint_id, status, admin_note)
            flash("Complaint updated successfully.", "success")
        else:
            flash("Please select a valid status.", "warning")

        return redirect(url_for("admin.complaints"))

    complaints = Complaint.list_all()
    return render_template("admin/complaints.html", complaints=complaints)


@admin_bp.route("/manage-students", methods=["GET", "POST"])
@admin_required
def manage_students():
    if request.method == "POST":
        if "add_student" in request.form:
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "").strip()
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            room_number = request.form.get("room_number", "").strip()

            if not username or not password or not name or not email:
                flash("All fields are required.", "warning")
            else:
                try:
                    Student.create(username, password, name, email, room_number)
                    flash("Student account created successfully.", "success")
                except sqlite3.IntegrityError:
                    flash("Username or email already exists.", "danger")

        if "delete_student" in request.form:
            student_id = request.form.get("student_id")
            if student_id:
                Student.delete(student_id)
                flash("Student removed successfully.", "success")

        return redirect(url_for("admin.manage_students"))

    students = Student.list_all()
    return render_template("admin/manage_students.html", students=students)


@admin_bp.route("/reports")
@admin_required
def reports():
    summary = Complaint.summary_by_status()
    return render_template("admin/reports.html", summary=summary)
