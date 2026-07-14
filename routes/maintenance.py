from flask import Blueprint, render_template, request, redirect, session, url_for
from utils.auth import admin_required
from utils.pdf_generator import generate_pdf
from utils.excel_generator import generate_excel
from models.maintenance import (
    get_all_maintenance,
    add_maintenance,
    get_maintenance_by_id,
    update_maintenance,
    delete_maintenance,
    search_maintenance
)

maintenance_bp = Blueprint("maintenance", __name__)


@maintenance_bp.route("/maintenance")
@admin_required
def maintenance():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    keyword = request.args.get("search")

    if keyword:
        maintenance_list = search_maintenance(keyword)
    else:
        maintenance_list = get_all_maintenance()

    return render_template(
        "maintenance.html",
        maintenance=maintenance_list
    )


# -----------------------------
# Add Maintenance
# -----------------------------
@maintenance_bp.route("/maintenance/add", methods=["GET", "POST"])
@admin_required
def add_maintenance_route():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        add_maintenance(
            request.form["maintenance_id"],
            request.form["asset_id"],
            request.form["engineer_name"],
            request.form["maintenance_date"],
            request.form["cost"],
            request.form["remarks"]
        )

        return redirect(url_for("maintenance.maintenance"))

    return render_template("maintenance_form.html")

@maintenance_bp.route("/maintenance/edit/<maintenance_id>", methods=["GET", "POST"])
@admin_required
def edit_maintenance(maintenance_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        update_maintenance(
            maintenance_id,
            request.form["asset_id"],
            request.form["engineer_name"],
            request.form["maintenance_date"],
            request.form["cost"],
            request.form["remarks"]
        )

        return redirect(url_for("maintenance.maintenance"))

    maintenance = get_maintenance_by_id(maintenance_id)

    return render_template(
        "maintenance_form.html",
        maintenance=maintenance,
        edit=True
    )

@maintenance_bp.route("/maintenance/delete/<maintenance_id>")
@admin_required
def delete_maintenance_route(maintenance_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))

    delete_maintenance(maintenance_id)

    return redirect(url_for("maintenance.maintenance"))

@maintenance_bp.route("/maintenance/export/excel")
@admin_required
def export_maintenance_excel():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    maintenance = get_all_maintenance()

    columns = [
        "Maintenance ID",
        "Asset ID",
        "Engineer Name",
        "Maintenance Date",
        "Cost",
        "Remarks"
    ]

    return generate_excel(
        data=maintenance,
        columns=columns,
        filename="maintenance_report.xlsx"
    )

@maintenance_bp.route("/maintenance/export/pdf")
@admin_required
def export_maintenance_pdf():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    maintenance = get_all_maintenance()

    headers = [
        "Maintenance ID",
        "Asset ID",
        "Engineer",
        "Date",
        "Cost",
        "Remarks"
    ]

    return generate_pdf(
        report_title="Maintenance Report",
        headers=headers,
        data=maintenance,
        filename="maintenance_report.pdf"
    )