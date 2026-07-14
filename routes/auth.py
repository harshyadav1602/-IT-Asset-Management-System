from flask import Blueprint, render_template, request, redirect, url_for, session
from models.auth import check_login, register_user
from database.db import get_connection
import random
from utils.email_service import send_otp
import bcrypt

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = check_login(username, password)

        if user:

            session["user"] = user[1]          # username
            session["user_id"] = user[0]       # database id
            session["full_name"] = user[3]     # full name
            session["role"] = user[4]          # role
            
            return redirect(url_for("dashboard.dashboard"))

        else:

            return render_template(
                "login.html",
                error="Invalid Username or Password"
            )

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():

    session.pop("user", None)
    session.pop("user_id", None)
    session.pop("full_name", None)
    session.pop("role", None)

    return redirect(url_for("auth.login"))

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        full_name = request.form["full_name"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:

            return render_template(
                "signup.html",
                error="Passwords do not match."
            )

        register_user(
            full_name,
            username,
            email,
            password
        )

        return redirect(url_for("auth.login"))

    return render_template("signup.html")

@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        # Database Connection
        conn = get_connection()
        cur = conn.cursor()

        # Check email exists
        cur.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cur.fetchone()

        cur.close()
        conn.close()

        if not user:

            return render_template(
                "forgot_password.html",
                error="Email not registered."
            )

        # Generate OTP
        otp = str(random.randint(100000,999999))

        # Save OTP and email in session
        session["otp"] = otp
        session["email"] = email

        # Send Email
        send_otp(email, otp)

        return redirect(url_for("auth.verify_otp"))

    return render_template("forgot_password.html")


@auth_bp.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():

    if request.method == "POST":

        otp = request.form["otp"]

        if otp == session.get("otp"):

            return redirect(url_for("auth.reset_password"))

        return render_template(
            "verify_otp.html",
            error="Invalid OTP"
        )

    return render_template("verify_otp.html")


@auth_bp.route("/reset-password", methods=["GET", "POST"])
def reset_password():

    if request.method == "POST":

        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:

            return render_template(
                "reset_password.html",
                error="Passwords do not match."
            )

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE users
            SET password=%s
            WHERE email=%s
        """, (
            hashed_password,
            session["email"]
        ))

        conn.commit()

        cur.close()
        conn.close()

        session.pop("otp", None)
        session.pop("email", None)

        return redirect(url_for("auth.login"))

    return render_template("reset_password.html")