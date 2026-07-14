import pandas as pd
from flask import app, send_file
from flask import Blueprint, render_template, request, redirect, url_for, session
from utils.pdf_generator import generate_pdf
from utils.excel_generator import generate_excel

from models.complaint import (
    get_all_complaints,
    add_complaint,
    get_complaint_by_id,
    update_complaint,
    delete_complaint,
    search_complaints
)

complaint_bp = Blueprint("complaint", __name__)

@complaint_bp.route("/complaints")
def complaints():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    keyword = request.args.get("search")

    if keyword:
        complaints = search_complaints(keyword)
    else:
        complaints = get_all_complaints()

    return render_template(
        "complaints.html",
        complaints=complaints
    )

@complaint_bp.route("/complaints/add", methods=["GET", "POST"])
def add_complaint_route():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        add_complaint(
            request.form["complaint_id"],
            request.form["employee_id"],
            request.form["asset_id"],
            request.form["issue"],
            request.form["complaint_date"],
            request.form["status"]
        )

        return redirect(url_for("complaint.complaints"))

    return render_template("complaint_form.html")

@complaint_bp.route("/complaints/edit/<complaint_id>", methods=["GET", "POST"])
def edit_complaint_route(complaint_id):

    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        employee_id = request.form["employee_id"]
        asset_id = request.form["asset_id"]
        issue = request.form["issue"]
        complaint_date = request.form["complaint_date"]
        status = request.form["status"]

        update_complaint(
            complaint_id,
            employee_id,
            asset_id,
            issue,
            complaint_date,
            status
        )

        return redirect(url_for("complaint.complaints"))

    complaint = get_complaint_by_id(complaint_id)

    return render_template(
        "complaint_form.html",
        complaint=complaint,
        edit=True
    )

@complaint_bp.route("/complaints/delete/<complaint_id>")
def delete_complaint_route(complaint_id):

    if "user" not in session:
        return redirect(url_for("auth.login"))

    delete_complaint(complaint_id)

    return redirect(url_for("complaint.complaints"))

@complaint_bp.route("/complaints/export/excel")
def export_complaint_excel():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    complaints = get_all_complaints()

    columns = [
        "Complaint ID",
        "Employee ID",
        "Asset ID",
        "Issue",
        "Complaint Date",
        "Status"
    ]

    return generate_excel(
        data=complaints,
        columns=columns,
        filename="complaint_report.xlsx"
    )

@complaint_bp.route("/complaints/export/pdf")
def export_complaint_pdf():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    complaints = get_all_complaints()

    headers = [
        "Complaint ID",
        "Employee ID",
        "Asset ID",
        "Issue",
        "Complaint Date",
        "Status"
    ]

    return generate_pdf(
        report_title="Complaint Report",
        headers=headers,
        data=complaints,
        filename="complaint_report.pdf"
    )
