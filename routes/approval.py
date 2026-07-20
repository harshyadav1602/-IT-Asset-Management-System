from flask import Blueprint, render_template, redirect, url_for, session
from psutil import users
from flask import request
from models.employee import get_all_employees
from models.approval import (
    get_pending_users,
    get_available_employees,
    approve_user,
    reject_user
)

approval_bp = Blueprint("approval", __name__)


# ============================
# Pending Users Page
# ============================
@approval_bp.route("/admin/user-approval")
def user_approval():

    # Only Admin can access
    if session.get("role") != "Admin":
        return redirect(url_for("auth.login"))

    users = get_pending_users()

    employees = get_available_employees()

    return render_template(
        "user_approval.html",
        users=users,
        employees=employees
    )


# ============================
# Approve User
# ============================
@approval_bp.route("/admin/approve/<int:user_id>", methods=["POST"])
def approve(user_id):

    if session.get("role") != "Admin":
        return redirect(url_for("auth.login"))

    role = request.form["role"]
    employee_id = request.form["employee_id"]

    approve_user(
        user_id,
        role,
        employee_id,
        session["user"]
    )

    return redirect(
        url_for("approval.user_approval")
    )


# ============================
# Reject User
# ============================
@approval_bp.route("/admin/reject/<int:user_id>")
def reject(user_id):

    if session.get("role") != "Admin":
        return redirect(url_for("auth.login"))

    reject_user(
        user_id,
        session["user"]
    )

    return redirect(
        url_for("approval.user_approval")
    )