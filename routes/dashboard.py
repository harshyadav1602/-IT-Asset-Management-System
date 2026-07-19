from flask import Blueprint, render_template, request, session, redirect, url_for
from database.db import get_connection
from utils.auth import admin_required
from models.dashboard import (
    dashboard_count,
    asset_category_chart,
    complaint_status_chart,
    maintenance_month_chart
)

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
@dashboard_bp.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    # Dashboard Cards
    data = dashboard_count()

    # Charts
    asset_chart = asset_category_chart()
    complaint_chart = complaint_status_chart()
    maintenance_chart = maintenance_month_chart()
    return render_template(
        "dashboard.html",
        total_employee=data["total_employee"],
        total_asset=data["total_asset"],
        total_complaint=data["total_complaint"],
        total_maintenance=data["total_maintenance"],
        asset_chart=asset_chart,
        complaint_chart=complaint_chart,
        maintenance_chart=maintenance_chart
    )

@dashboard_bp.route("/admin-profile")
@admin_required
def admin_profile():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            full_name,
            username,
            email,
            role,
            phone,
            profile_photo
        FROM users
        WHERE username=%s
    """, (session["user"],))

    admin = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        "admin_profile.html",
        admin=admin
    )

@dashboard_bp.route("/edit-admin-profile", methods=["GET", "POST"])
@admin_required
def edit_admin_profile():

    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":

        email = request.form["email"]
        phone = request.form["phone"]

        cur.execute("""
            UPDATE users
            SET email=%s,
                phone=%s
            WHERE username=%s
        """, (
            email,
            phone,
            session["user"]
        ))

        conn.commit()

        cur.close()
        conn.close()

        return redirect(url_for("dashboard.admin_profile"))

    cur.execute("""
        SELECT
            full_name,
            username,
            role,
            email,
            phone
        FROM users
        WHERE username=%s
    """, (session["user"],))

    admin = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        "edit_admin_profile.html",
        admin=admin
    )