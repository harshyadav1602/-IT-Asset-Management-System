from flask import app, send_file
from reportlab.pdfgen.canvas import Canvas
import os
import pandas as pd
from flask import Blueprint, render_template, request, session, redirect, url_for
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
def delete(employee_id):

    if "user" not in session:
        return redirect(url_for("auth.login"))

    delete_employee(employee_id)

    return redirect("/employees")


# for excel export
@employee_bp.route("/employees/export/excel")
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
def export_employee_pdf():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    employees = get_all_employees()

    os.makedirs("exports", exist_ok=True)
    filepath = "exports/employee_report.pdf"

    c = Canvas(filepath)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 800, "Employee Report")

    y = 760

    c.setFont("Helvetica", 10)

    for emp in employees:

        c.drawString(
            40,
            y,
            f"{emp[0]}   {emp[1]}   {emp[2]}   {emp[3]}"
        )

        y -= 20

        if y < 50:
            c.showPage()
            y = 800

    c.save()

    return send_file(filepath, as_attachment=True)
