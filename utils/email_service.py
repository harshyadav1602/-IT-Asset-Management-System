import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your Gmail
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

# Replace with your Gmail App Password
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_otp(email, otp):

    subject = "Password Reset OTP"

    body = f"""
Hello,

Your OTP is:

{otp}

This OTP is valid for 5 minutes.

Do not share this OTP with anyone.

Regards,
IT Asset Management System
"""

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(
        EMAIL_ADDRESS,
        EMAIL_PASSWORD
    )

    server.sendmail(
        EMAIL_ADDRESS,
        email,
        msg.as_string()
    )

    server.quit()