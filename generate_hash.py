import bcrypt

password = "admin123"

hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

print(hashed.decode("utf-8"))
print("Length:", len(hashed.decode("utf-8")))