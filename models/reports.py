from database.db import get_connection

def get_employee_report():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            employee_id,
            employee_name,
            department_id,
            designation,
            email,
            phone
        FROM employee
        ORDER BY employee_id

    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_asset_report():
    conn = get_connection()
    cur =  conn.cursor()
    cur.execute("""
        SELECT
            asset_id,
            asset_name,
            category,
            brand,
            model,
            status,
            employee_id
        FROM asset
        ORDER BY asset_id
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_complaint_report():
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
        ORDER BY complaint_id
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_maintenance_report():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            maintenance_id,
            asset_id,
            maintenance_date,
            engineer_name,
            cost,
            remarks
        FROM maintenance
        ORDER BY maintenance_id
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data