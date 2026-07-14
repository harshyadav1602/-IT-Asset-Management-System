from database.db import get_connection

def get_all_employees():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT employee_id,
               employee_name,
               department_id,
               designation,
               email,
               phone
        FROM employee
        ORDER BY employee_name;
    """)

    employees = cur.fetchall()

    cur.close()
    conn.close()

    return employees

def add_employee(employee_id, employee_name, department_id,
                 designation, email, phone):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO employee
        (
            employee_id,
            employee_name,
            department_id,
            designation,
            email,
            phone
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """,
    (
        employee_id,
        employee_name,
        department_id,
        designation,
        email,
        phone
    ))

    conn.commit()

    cur.close()
    conn.close()

def get_employee_by_id(employee_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT employee_id,
               employee_name,
               department_id,
               designation,
               email,
               phone
        FROM employee
        WHERE employee_id = %s
    """, (employee_id,))

    employee = cur.fetchone()

    cur.close()
    conn.close()

    return employee


def update_employee(employee_id, employee_name,
                    department_id, designation,
                    email, phone):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE employee
        SET
            employee_name=%s,
            department_id=%s,
            designation=%s,
            email=%s,
            phone=%s
        WHERE employee_id=%s
    """, (
        employee_name,
        department_id,
        designation,
        email,
        phone,
        employee_id
    ))

    conn.commit()

    cur.close()
    conn.close()

def delete_employee(employee_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM employee
        WHERE employee_id=%s
    """, (employee_id,))

    conn.commit()
    cur.close()
    conn.close()

def search_employee(keyword):

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
        WHERE

        employee_name ILIKE %s

        OR employee_id ILIKE %s

        OR designation ILIKE %s
    """,
    (
        "%" + keyword + "%",
        "%" + keyword + "%",
        "%" + keyword + "%"
    ))

    employees = cur.fetchall()

    cur.close()
    conn.close()

    return employees

# ==========================================
# Get Employee Profile
# ==========================================

def get_employee_profile(employee_id):

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
        WHERE employee_id=%s
    """, (employee_id,))

    employee = cur.fetchone()

    cur.close()
    conn.close()

    return employee

# ===================================
# Update Employee Profile
# ===================================

def update_employee_profile(employee_id,
                            email,
                            phone):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

        UPDATE employee

        SET

            email=%s,

            phone=%s

        WHERE employee_id=%s

    """,
    (
        email,
        phone,
        employee_id
    ))

    conn.commit()

    cur.close()

    conn.close()