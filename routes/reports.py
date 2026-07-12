from flask import Blueprint, render_template
from models.reports import get_asset_report, get_complaint_report, get_employee_report, get_maintenance_report
from flask import send_file
from flask import request
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
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

    df = pd.DataFrame(
        employees,
        columns=[
            "Employee ID",
            "Employee Name",
            "Department ID",
            "Designation",
            "Email",
            "Phone"
        ]
    )
    os.makedirs("exports", exist_ok=True)
    file_path = "exports/Employee_Report.xlsx"
    df.to_excel(file_path, index=False)
    return send_file(file_path, as_attachment=True)

@reports_bp.route("/employee_report/pdf")
def employee_report_pdf():
    employees = get_employee_report()
    os.makedirs("exports", exist_ok=True)
    pdf_path = "exports/Employee_Report.pdf"
    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    elements = []
    title = Paragraph("<b>IT Asset Management System</b>", styles['Title'])
    subtitle = Paragraph("<b>Employee Report</b>", styles['Heading2'])
    elements.append(title)
    elements.append(subtitle)
    elements.append(Paragraph("<br/>", styles['Normal']))
    data = [[
        "ID",
        "Name",
        "Department",
        "Designation",
        "Email",
        "Phone"
    ]]
    for emp in employees:
        data.append([
            emp[0],
            emp[1],
            emp[2],
            emp[3],
            emp[4],
            emp[5]
        ])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 10)
    ]))
    elements.append(table)
    doc.build(elements)
    return send_file(pdf_path, as_attachment=True)

@reports_bp.route("/asset_report")
def asset_report():

    assets = get_asset_report()
    return render_template(
        "asset_report.html",
        assets=assets,
        total_asset=len(assets)
    )

@reports_bp.route("/complaint_report")
def complaint_report():

    complaints = get_complaint_report()

    return render_template(
        "complaint_report.html",
        complaints=complaints,
        total_complaint=len(complaints)
    )

@reports_bp.route("/maintenance_report")
def maintenance_report():

    maintenance = get_maintenance_report()

    return render_template(
        "maintenance_report.html",
        maintenance=maintenance,
        total_maintenance=len(maintenance)
    )