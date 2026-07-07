from flask import Blueprint, render_template, request, redirect, url_for
from flask import session, flash

from models.student import Student
from models.complaint import Complaint


student = Blueprint("student", __name__, url_prefix="/student")


# ---------------------------------------
# Student Dashboard
# ---------------------------------------

@student.route("/dashboard")
def dashboard():

    if session.get("role") != "student":

        return redirect(url_for("auth.home"))


    student_id = session.get("id")


    data = {

        "total": Student.complaint_count(student_id),

        "pending": Student.pending_count(student_id),

        "progress": Student.progress_count(student_id),

        "resolved": Student.resolved_count(student_id)

    }


    complaints = Complaint.get_by_student(student_id)


    return render_template(

        "student/dashboard.html",

        stats=data,

        complaints=complaints

    )


# ---------------------------------------
# Submit Complaint
# ---------------------------------------

@student.route("/submit", methods=["GET","POST"])
def submit_complaint():


    if session.get("role") != "student":

        return redirect(url_for("auth.home"))



    if request.method == "POST":


        Complaint.create(

            session.get("id"),

            request.form.get("title"),

            request.form.get("category"),

            request.form.get("description"),

            request.form.get("priority","Medium"),

            None

        )


        flash(

            "Complaint submitted successfully.",

            "success"

        )


        return redirect(

            url_for("student.dashboard")

        )



    return render_template(

        "student/submit_complaint.html"

    )



# ---------------------------------------
# Complaint History
# ---------------------------------------

@student.route("/history")
def complaint_history():


    if session.get("role") != "student":

        return redirect(url_for("auth.home"))



    complaints = Complaint.get_by_student(

        session.get("id")

    )


    return render_template(

        "student/complaint_history.html",

        complaints=complaints

    )



# ---------------------------------------
# Profile
# ---------------------------------------

@student.route("/profile")
def profile():


    if session.get("role") != "student":

        return redirect(url_for("auth.home"))



    student_data = Student.get(

        session.get("id")

    )


    return render_template(

        "student/profile.html",

        student=student_data

    )



# ---------------------------------------
# Update Profile
# ---------------------------------------

@student.route("/profile/update", methods=["POST"])
def update_profile():


    if session.get("role") != "student":

        return redirect(url_for("auth.home"))



    Student.update(

        session.get("id"),

        request.form.get("name"),

        request.form.get("email"),

        request.form.get("room_number"),

        request.form.get("phone")

    )


    flash(

        "Profile updated successfully.",

        "success"

    )


    return redirect(

        url_for("student.profile")

    )