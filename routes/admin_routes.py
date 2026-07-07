from flask import Blueprint, render_template, request, redirect, url_for
from flask import session, flash

from models.complaint import Complaint
from models.student import Student


admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


# ---------------------------------------
# Admin Access Check
# ---------------------------------------

def check_admin():

    return session.get("role") == "admin"



# ---------------------------------------
# Dashboard
# ---------------------------------------

@admin.route("/dashboard")
def dashboard():

    if not check_admin():

        return redirect(url_for("auth.home"))


    stats = {

        "total_complaints": Complaint.total(),

        "pending": Complaint.pending(),

        "progress": Complaint.progress(),

        "resolved": Complaint.resolved(),

        "students": Student.total()

    }


    recent = Complaint.get_all()[:5]


    return render_template(

        "admin/dashboard.html",

        stats=stats,

        complaints=recent

    )



# ---------------------------------------
# All Complaints
# ---------------------------------------

@admin.route("/complaints")
def complaints():

    if not check_admin():

        return redirect(url_for("auth.home"))


    data = Complaint.get_all()


    return render_template(

        "admin/complaints.html",

        complaints=data

    )



# ---------------------------------------
# Update Complaint Status
# ---------------------------------------

@admin.route(
    "/complaint/update/<int:id>",
    methods=["POST"]
)
def update_complaint(id):


    if not check_admin():

        return redirect(url_for("auth.home"))



    status = request.form.get("status")


    Complaint.update_status(

        id,

        status

    )


    flash(

        "Complaint status updated.",

        "success"

    )


    return redirect(

        url_for("admin.complaints")

    )



# ---------------------------------------
# Delete Complaint
# ---------------------------------------

@admin.route(
    "/complaint/delete/<int:id>"
)
def delete_complaint(id):


    if not check_admin():

        return redirect(url_for("auth.home"))



    Complaint.delete(id)


    flash(

        "Complaint deleted successfully.",

        "success"

    )


    return redirect(

        url_for("admin.complaints")

    )



# ---------------------------------------
# Manage Students
# ---------------------------------------

@admin.route("/students")
def manage_students():


    if not check_admin():

        return redirect(url_for("auth.home"))



    students = Student.get_all()



    return render_template(

        "admin/manage_students.html",

        students=students

    )



# ---------------------------------------
# Delete Student
# ---------------------------------------

@admin.route(
    "/student/delete/<int:id>"
)
def delete_student(id):


    if not check_admin():

        return redirect(url_for("auth.home"))



    Student.delete(id)


    flash(

        "Student removed.",

        "success"

    )


    return redirect(

        url_for("admin.manage_students")

    )



# ---------------------------------------
# Reports
# ---------------------------------------

@admin.route("/reports")
def reports():


    if not check_admin():

        return redirect(url_for("auth.home"))



    category_data = Complaint.category_report()


    monthly_data = Complaint.monthly_report()



    return render_template(

        "admin/reports.html",

        categories=category_data,

        monthly=monthly_data

    )