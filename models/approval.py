from database.db import get_connection


def get_pending_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            user_id,
            username,
            full_name,
            email,
            role,
            approval_status
        FROM users
        WHERE LOWER(approval_status) = 'pending'
        ORDER BY user_id;
    """)

    users = cur.fetchall()

    cur.close()
    conn.close()

    return users


def approve_user(user_id, role, employee_id, admin_name):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET
            role=%s,
            employee_id=%s,
            approval_status='Approved',
            approved_by=%s,
            approved_date=NOW()
        WHERE user_id=%s
    """, (
        role,
        employee_id,
        admin_name,
        user_id
    ))

    conn.commit()

    cur.close()
    conn.close()


def reject_user(user_id, admin_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET
            approval_status='Rejected',
            approved_by=%s,
            approved_date=NOW()
        WHERE user_id=%s
    """, (admin_name, user_id))

    conn.commit()

    cur.close()
    conn.close()

def get_available_employees():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            e.employee_id,
            e.employee_name
        FROM employee e
        WHERE e.employee_id NOT IN
        (
            SELECT employee_id
            FROM users
            WHERE employee_id IS NOT NULL
        )
        ORDER BY e.employee_name
    """)

    employees = cur.fetchall()

    cur.close()
    conn.close()

    return employees

def get_pending_count():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM users
        WHERE LOWER(approval_status)='pending'
    """)

    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return count