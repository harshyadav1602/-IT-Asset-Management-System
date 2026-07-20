from database.db import get_connection

def dashboard_count():

    conn = get_connection()
    cur = conn.cursor()

    # Employee Count
    cur.execute("SELECT COUNT(*) FROM employee")
    total_employee = cur.fetchone()[0]

    # Asset Count
    cur.execute("SELECT COUNT(*) FROM asset")
    total_asset = cur.fetchone()[0]

    # Complaint Count
    cur.execute("SELECT COUNT(*) FROM complaint")
    total_complaint = cur.fetchone()[0]

    # Maintenance Count
    cur.execute("SELECT COUNT(*) FROM maintenance")
    total_maintenance = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "total_employee": total_employee,
        "total_asset": total_asset,
        "total_complaint": total_complaint,
        "total_maintenance": total_maintenance
    }


def asset_category_chart():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

        SELECT
            category,
            COUNT(*)

        FROM asset

        GROUP BY category

        ORDER BY category

    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data


def complaint_status_chart():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

        SELECT
            status,
            COUNT(*)

        FROM complaint

        GROUP BY status

        ORDER BY status

    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data


def maintenance_month_chart():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

        SELECT
            TO_CHAR(maintenance_date,'Mon'),
            COUNT(*)

        FROM maintenance

        GROUP BY
            DATE_TRUNC('month',maintenance_date),
            TO_CHAR(maintenance_date,'Mon')

        ORDER BY
            DATE_TRUNC('month',maintenance_date)

    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data

# ==========================================
# Pending User Approval Count
# ==========================================

def get_pending_user_count():

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