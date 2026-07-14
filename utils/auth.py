from flask import session, redirect, url_for, flash
from functools import wraps


# ==========================================
# LOGIN REQUIRED
# ==========================================

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user" not in session:
            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return decorated_function


# ==========================================
# ADMIN REQUIRED
# ==========================================

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user" not in session:
            return redirect(url_for("auth.login"))

        if session.get("role") != "Admin":
            flash("Access Denied!")
            return redirect(url_for("dashboard.dashboard"))

        return f(*args, **kwargs)

    return decorated_function


# ==========================================
# EMPLOYEE REQUIRED
# ==========================================

def employee_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user" not in session:
            return redirect(url_for("auth.login"))

        if session.get("role") != "Employee":
            flash("Access Denied!")
            return redirect(url_for("dashboard.dashboard"))

        return f(*args, **kwargs)

    return decorated_function