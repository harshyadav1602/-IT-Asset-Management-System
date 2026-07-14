from flask import Blueprint, render_template, session, redirect, url_for
from flask import request
from utils.auth import employee_required
from models.asset import get_assets_by_employee
from models.complaint import get_complaints_by_employee
from models.employee import get_employee_profile
from models.employee import update_employee_profile
from models.complaint import add_employee_complaint
from models.asset import get_employee_asset_list
from database.db import get_connection
import bcrypt
from flask import flash
from models.auth import (
    get_password_by_username,
    update_password
)

employee_portal_bp = Blueprint("employee_portal", __name__)

def get_employee_id(username):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT employee_id
        FROM employee
        WHERE email = (
            SELECT email
            FROM users
            WHERE username=%s
        )
    """, (username,))

    employee = cur.fetchone()

    cur.close()
    conn.close()

    if employee:
        return employee[0]

    return None

@employee_portal_bp.route("/my-assets")
@employee_required
def my_assets():

    username = session["user"]

    employee_id = get_employee_id(username)

    assets = get_assets_by_employee(employee_id)

    return render_template(
        "my_assets.html",
        assets=assets
    )

@employee_portal_bp.route("/my-complaints")
@employee_required
def my_complaints():

    username = session["user"]

    employee_id = get_employee_id(username)

    complaints = get_complaints_by_employee(employee_id)

    return render_template(
        "my_complaints.html",
        complaints=complaints
    )

@employee_portal_bp.route("/my-profile")
@employee_required
def my_profile():

    username = session["user"]

    employee_id = get_employee_id(username)

    employee = get_employee_profile(employee_id)

    return render_template(
        "my_profile.html",
        employee=employee
    )

@employee_portal_bp.route(
    "/edit-my-profile",
    methods=["GET","POST"]
)
@employee_required
def edit_my_profile():

    username = session["user"]

    employee_id = get_employee_id(username)

    employee = get_employee_profile(employee_id)

    if request.method == "POST":

        email = request.form["email"]

        phone = request.form["phone"]

        update_employee_profile(
            employee_id,
            email,
            phone
        )

        return redirect(url_for(
            "employee_portal.my_profile"
        ))

    return render_template(
        "edit_my_profile.html",
        employee=employee
    )

@employee_portal_bp.route(
    "/change-password",
    methods=["GET","POST"]
)
@employee_required
def change_password():

    if request.method == "POST":

        current_password = request.form["current_password"]

        new_password = request.form["new_password"]

        confirm_password = request.form["confirm_password"]

        username = session["user"]

        user = get_password_by_username(username)

        if not bcrypt.checkpw(
            current_password.encode(),
            user[0].encode()
        ):

            flash("Current password is incorrect.")

            return redirect(
                url_for("employee_portal.change_password")
            )

        if new_password != confirm_password:

            flash("Passwords do not match.")

            return redirect(
                url_for("employee_portal.change_password")
            )

        update_password(
            username,
            new_password
        )

        flash("Password changed successfully!")

        return redirect(
            url_for("employee_portal.my_profile")
        )

    return render_template(
        "change_password.html"
    )

@employee_portal_bp.route(
    "/raise-complaint",
    methods=["GET","POST"]
)
@employee_required
def raise_complaint():

    username = session["user"]
    print("Username:", username)

    employee_id = get_employee_id(username)
    print("Employee ID:", employee_id)

    assets = get_employee_asset_list(employee_id)
    print("Assets:", assets)

    if request.method == "POST":

        asset_id = request.form["asset_id"]

        issue = request.form["issue"]

        add_employee_complaint(
            employee_id,
            asset_id,
            issue
        )

        return redirect(
            url_for("employee_portal.my_complaints")
        )

    return render_template(
        "raise_complaint.html",
        assets=assets
    )