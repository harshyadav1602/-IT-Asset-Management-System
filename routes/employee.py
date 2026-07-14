from flask import app, send_file
from utils.pdf_generator import generate_pdf
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os
import pandas as pd
from flask import Blueprint, render_template, request, session, redirect, url_for
from utils.auth import admin_required
from models.employee import (
    get_all_employees,
    add_employee,
    get_employee_by_id,
    update_employee,
    delete_employee,
    search_employee
)

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/employees")
@admin_required
def employees():

    if "user" not in session:
        return redirect(url_for("auth.login"))
    keyword = request.args.get("search")
    if keyword:
        employee_list = search_employee(keyword)
    else:
        employee_list = get_all_employees()

    return render_template(
        "employees.html",
        employees=employee_list
    )

@employee_bp.route("/employees/add", methods=["GET", "POST"])
@admin_required
def add_employee_route():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        employee_id = request.form["employee_id"]
        employee_name = request.form["employee_name"]
        department_id = request.form["department_id"]
        designation = request.form["designation"]
        email = request.form["email"]
        phone = request.form["phone"]

        add_employee(
            employee_id,
            employee_name,
            department_id,
            designation,
            email,
            phone
        )

        return redirect(url_for("employee.employees"))

    return render_template("employee_form.html")

@employee_bp.route("/employees/edit/<employee_id>", methods=["GET", "POST"])
@admin_required
def edit_employee(employee_id):

    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        employee_name = request.form["employee_name"]
        department_id = request.form["department_id"]
        designation = request.form["designation"]
        email = request.form["email"]
        phone = request.form["phone"]

        update_employee(
            employee_id,
            employee_name,
            department_id,
            designation,
            email,
            phone
        )

        return redirect(url_for("employee.employees"))

    employee = get_employee_by_id(employee_id)

    return render_template(
        "employee_form.html",
        employee=employee,
        edit=True
    )

@employee_bp.route("/employees/delete/<employee_id>")
@admin_required
def delete(employee_id):

    if "user" not in session:
        return redirect(url_for("auth.login"))

    delete_employee(employee_id)

    return redirect("/employees")


# for excel export
@employee_bp.route("/employees/export/excel")
@admin_required
def export_employee_excel():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    employees = get_all_employees()

    df = pd.DataFrame(
        employees,
        columns=[
            "Employee ID",
            "Employee Name",
            "Department",
            "Designation",
            "Email",
            "Phone"
        ]
    )

    filepath = "exports/employee_report.xlsx"
    df.to_excel(filepath, index=False)
    return send_file(filepath, as_attachment=True)

@employee_bp.route("/employees/export/pdf")
@admin_required
def export_employee_pdf():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    employees = get_all_employees()

    headers = [
        "Employee ID",
        "Employee Name",
        "Department",
        "Designation",
        "Email",
        "Phone"
    ]

    return generate_pdf(
        report_title="Employee Report",
        headers=headers,
        data=employees,
        filename="employee_report.pdf"
    )