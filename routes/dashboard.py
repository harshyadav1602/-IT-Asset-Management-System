from flask import Blueprint, render_template, session, redirect, url_for
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