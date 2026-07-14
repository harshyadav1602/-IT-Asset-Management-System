from flask import Flask, redirect, render_template, session, url_for
from database.db import get_connection
from routes.dashboard import dashboard_bp
from routes.employee import employee_bp
from routes.asset import asset_bp
from routes.complaint import complaint_bp
from routes.maintenance import maintenance_bp
from routes.auth import auth_bp
from routes.reports import reports_bp
from routes.employee_portal import employee_portal_bp

app = Flask(__name__)
app.secret_key = "harsh_project_secret_key"
app.register_blueprint(dashboard_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(asset_bp)
app.register_blueprint(complaint_bp)
app.register_blueprint(maintenance_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(employee_portal_bp)

@app.route("/")
def home():

    conn = get_connection()
    cursor = conn.cursor()

    # Employee list
    cursor.execute("""
        SELECT employee_id,
               employee_name,
               designation
        FROM employee
        ORDER BY employee_name
    """)
    employees = cursor.fetchall()

    # Dashboard counts
    cursor.execute("SELECT COUNT(*) FROM employee")
    total_employee = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM asset")
    total_asset = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM complaint")
    total_complaint = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM maintenance")
    total_maintenance = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        employees=employees,
        total_employee=total_employee,
        total_asset=total_asset,
        total_complaint=total_complaint,
        total_maintenance=total_maintenance
    )

@app.route("/logout")
def logout():
    session.clear()      # Remove all session data
    return redirect(url_for("auth.login"))

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run(debug=True)