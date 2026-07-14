from database.db import get_connection

def get_all_complaints():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            complaint_id,
            employee_id,
            asset_id,
            issue,
            complaint_date,
            status
        FROM complaint
        ORDER BY complaint_date DESC
    """)

    complaints = cur.fetchall()

    cur.close()
    conn.close()

    return complaints


def add_complaint(
    complaint_id,
    employee_id,
    asset_id,
    issue,
    complaint_date,
    status
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO complaint
        (
            complaint_id,
            employee_id,
            asset_id,
            issue,
            complaint_date,
            status
        )
        VALUES (%s,%s,%s,%s,%s,%s)
    """,
    (
        complaint_id,
        employee_id,
        asset_id,
        issue,
        complaint_date,
        status
    ))

    conn.commit()

    cur.close()
    conn.close()

def get_complaint_by_id(complaint_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            complaint_id,
            employee_id,
            asset_id,
            issue,
            complaint_date,
            status
        FROM complaint
        WHERE complaint_id = %s
    """, (complaint_id,))

    complaint = cur.fetchone()

    cur.close()
    conn.close()

    return complaint

def update_complaint(
    complaint_id,
    employee_id,
    asset_id,
    issue,
    complaint_date,
    status
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE complaint
        SET
            employee_id=%s,
            asset_id=%s,
            issue=%s,
            complaint_date=%s,
            status=%s
        WHERE complaint_id=%s
    """,
    (
        employee_id,
        asset_id,
        issue,
        complaint_date,
        status,
        complaint_id
    ))

    conn.commit()

    cur.close()
    conn.close()

def delete_complaint(complaint_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM complaint WHERE complaint_id=%s",
        (complaint_id,)
    )

    conn.commit()

    cur.close()
    conn.close()

def search_complaints(keyword):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            complaint_id,
            employee_id,
            asset_id,
            issue,
            complaint_date,
            status
        FROM complaint
        WHERE
            complaint_id ILIKE %s OR
            employee_id ILIKE %s OR
            asset_id ILIKE %s OR
            issue ILIKE %s OR
            status ILIKE %s
    """,
    (
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%'
    ))

    complaints = cur.fetchall()

    cur.close()
    conn.close()

    return complaints

# ==================================
# Get Complaints By Employee
# ==================================

def get_complaints_by_employee(employee_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            complaint_id,
            employee_id,
            asset_id,
            issue,
            complaint_date,
            status
        FROM complaint
        WHERE employee_id=%s
        ORDER BY complaint_date DESC
    """, (employee_id,))

    complaints = cur.fetchall()

    cur.close()
    conn.close()

    return complaints

from datetime import date

# ==========================================
# Employee Raise Complaint
# ==========================================

def add_employee_complaint(employee_id, asset_id, issue):

    conn = get_connection()
    cur = conn.cursor()

    # Generate next Complaint ID
    cur.execute("""
        SELECT complaint_id
        FROM complaint
        ORDER BY complaint_id DESC
        LIMIT 1
    """)

    last = cur.fetchone()

    if last:
        number = int(last[0][3:]) + 1
    else:
        number = 1

    complaint_id = f"CMP{number:03d}"

    cur.execute("""
        INSERT INTO complaint
        (
            complaint_id,
            employee_id,
            asset_id,
            issue,
            complaint_date,
            status
        )
        VALUES (%s,%s,%s,%s,%s,%s)
    """,
    (
        complaint_id,
        employee_id,
        asset_id,
        issue,
        date.today(),
        "Pending"
    ))

    conn.commit()

    cur.close()
    conn.close()