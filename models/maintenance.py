from database.db import get_connection


def get_all_maintenance():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            maintenance_id,
            asset_id,
            engineer_name,
            maintenance_date,
            cost,
            remarks
        FROM maintenance
        ORDER BY maintenance_date DESC
    """)

    maintenance = cur.fetchall()

    cur.close()
    conn.close()

    return maintenance


def add_maintenance(
    maintenance_id,
    asset_id,
    engineer_name,
    maintenance_date,
    cost,
    remarks
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO maintenance
        (
            maintenance_id,
            asset_id,
            engineer_name,
            maintenance_date,
            cost,
            remarks
        )
        VALUES (%s,%s,%s,%s,%s,%s)
    """,
    (
        maintenance_id,
        asset_id,
        engineer_name,
        maintenance_date,
        cost,
        remarks
    ))

    conn.commit()

    cur.close()
    conn.close()

def get_maintenance_by_id(maintenance_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            maintenance_id,
            asset_id,
            engineer_name,
            maintenance_date,
            cost,
            remarks
        FROM maintenance
        WHERE maintenance_id=%s
    """, (maintenance_id,))

    maintenance = cur.fetchone()

    cur.close()
    conn.close()

    return maintenance


def update_maintenance(
    maintenance_id,
    asset_id,
    engineer_name,
    maintenance_date,
    cost,
    remarks
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE maintenance
        SET
            asset_id=%s,
            engineer_name=%s,
            maintenance_date=%s,
            cost=%s,
            remarks=%s
        WHERE maintenance_id=%s
    """,
    (
        asset_id,
        engineer_name,
        maintenance_date,
        cost,
        remarks,
        maintenance_id
    ))

    conn.commit()

    cur.close()
    conn.close()


def delete_maintenance(maintenance_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM maintenance WHERE maintenance_id=%s",
        (maintenance_id,)
    )

    conn.commit()

    cur.close()
    conn.close()

def search_maintenance(keyword):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            maintenance_id,
            asset_id,
            engineer_name,
            maintenance_date,
            cost,
            remarks
        FROM maintenance
        WHERE
            maintenance_id ILIKE %s OR
            asset_id ILIKE %s OR
            engineer_name ILIKE %s OR
            remarks ILIKE %s
    """,
    (
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%'
    ))

    maintenance = cur.fetchall()

    cur.close()
    conn.close()

    return maintenance