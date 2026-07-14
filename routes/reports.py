from flask import Blueprint, render_template
from models.reports import get_asset_report, get_complaint_report, get_employee_report, get_maintenance_report
from flask import send_file
from flask import request
from utils.pdf_generator import generate_pdf
from utils.excel_generator import generate_excel
import pandas as pd
import os

reports_bp = Blueprint("reports", __name__)

@reports_bp.route("/reports")
def reports():

    return render_template("reports.html")

@reports_bp.route("/employee_report")
def employee_report():
    employees = get_employee_report()
    return render_template(
        "employee_report.html",
        employees=employees,
        total_employee=len(employees)
    )

@reports_bp.route("/employee_report/excel")
def employee_report_excel():

    employees = get_employee_report()

    columns = [
        "Employee ID",
        "Employee Name",
        "Department ID",
        "Designation",
        "Email",
        "Phone"
    ]

    return generate_excel(
        data=employees,
        columns=columns,
        filename="Employee_Report.xlsx"
    )

@reports_bp.route("/employee_report/pdf")
def employee_report_pdf():

    employees = get_employee_report()

    headers = [
        "Employee ID",
        "Employee Name",
        "Department ID",
        "Designation",
        "Email",
        "Phone"
    ]

    return generate_pdf(
        report_title="Employee Report",
        headers=headers,
        data=employees,
        filename="Employee_Report.pdf"
    )

@reports_bp.route("/asset_report")
def asset_report():

    assets = get_asset_report()
    return render_template(
        "asset_report.html",
        assets=assets,
        total_asset=len(assets)
    )

@reports_bp.route("/asset_report/excel")
def asset_report_excel():

    assets = get_asset_report()

    columns = [
        "Asset ID",
        "Asset Name",
        "Category",
        "Brand",
        "Model",
        "Status",
        "Employee ID"
    ]

    return generate_excel(
        data=assets,
        columns=columns,
        filename="Asset_Report.xlsx"
    )

@reports_bp.route("/asset_report/pdf")
def asset_report_pdf():

    assets = get_asset_report()

    headers = [
        "Asset ID",
        "Asset Name",
        "Category",
        "Brand",
        "Model",
        "Status",
        "Employee ID"
    ]

    return generate_pdf(
        report_title="Asset Report",
        headers=headers,
        data=assets,
        filename="Asset_Report.pdf"
    )


@reports_bp.route("/complaint_report")
def complaint_report():

    complaints = get_complaint_report()

    return render_template(
        "complaint_report.html",
        complaints=complaints,
        total_complaint=len(complaints)
    )

@reports_bp.route("/complaint_report/excel")
def complaint_report_excel():

    complaints = get_complaint_report()

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
        filename="Complaint_Report.xlsx"
    )

@reports_bp.route("/complaint_report/pdf")
def complaint_report_pdf():

    complaints = get_complaint_report()

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
        filename="Complaint_Report.pdf"
    )

@reports_bp.route("/maintenance_report")
def maintenance_report():

    maintenance = get_maintenance_report()

    return render_template(
        "maintenance_report.html",
        maintenance=maintenance,
        total_maintenance=len(maintenance)
    )

@reports_bp.route("/maintenance_report/excel")
def maintenance_report_excel():

    maintenance = get_maintenance_report()

    columns = [
        "Maintenance ID",
        "Asset ID",
        "Engineer",
        "Date",
        "Cost",
        "Remarks"
    ]

    return generate_excel(
        data=maintenance,
        columns=columns,
        filename="Maintenance_Report.xlsx"
    )

@reports_bp.route("/maintenance_report/pdf")
def maintenance_report_pdf():

    maintenance = get_maintenance_report()

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
        filename="Maintenance_Report.pdf"
    )