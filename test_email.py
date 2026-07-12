from utils.email_service import send_otp

send_otp(
    "recipient@gmail.com",
    "123456"
)

print("Email Sent Successfully")