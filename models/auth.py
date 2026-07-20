from database.db import get_connection
import bcrypt


def check_login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM users
        WHERE username=%s
    """, (username,))

    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        stored_password = user[2]
        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password.encode("utf-8")
        ):
            # approval_status is the new column
            # We fetch it by name to avoid index issues
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("""
                SELECT approval_status
                FROM users
                WHERE username=%s
            """, (username,))

            status = cur.fetchone()[0]

            cur.close()
            conn.close()

            if status != "Approved":
                return "PENDING"

            return user

    return None


# ============================================
# REGISTER USER
# ============================================


def register_user(full_name, username, email, password):
    conn = get_connection()
    cur = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    cur.execute("""
        INSERT INTO users
        (username, password, full_name, email, approval_status)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        username,
        hashed_password,
        full_name,
        email,
        "pending"
    ))

    conn.commit()

    cur.close()
    conn.close()


# ==========================================
# Get Password By Username
# ==========================================


def get_password_by_username(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT password
        FROM users
        WHERE username=%s
    """, (username,))

    user = cur.fetchone()

    cur.close()
    conn.close()

    return user


# ==========================================
# Update Password
# ==========================================


def update_password(username, new_password):
    conn = get_connection()
    cur = conn.cursor()

    hashed_password = bcrypt.hashpw(
        new_password.encode(),
        bcrypt.gensalt()
    ).decode()

    cur.execute("""
        UPDATE users
        SET password=%s
        WHERE username=%s
    """,
                (
                    hashed_password,
                    username
                ))

    conn.commit()

    cur.close()
    conn.close()


def update_profile_photo(username, filename):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET profile_photo=%s
        WHERE username=%s
    """, (filename, username))

    conn.commit()

    cur.close()
    conn.close()


def get_profile_photo(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT profile_photo
        FROM users
        WHERE username=%s
    """, (username,))

    photo = cur.fetchone()

    cur.close()
    conn.close()

    return photo