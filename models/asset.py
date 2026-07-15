from database.db import get_connection


# ==========================
# Get All Assets
# ==========================
def get_all_assets():
    conn = get_connection()
    cur = conn.cursor()

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
        ORDER BY asset_id;
    """)

    assets = cur.fetchall()

    cur.close()
    conn.close()

    return assets


# ==========================
# Add Asset
# ==========================
def add_asset(asset_id, asset_name, category,
              brand, model, status, employee_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO asset
        (
            asset_id,
            asset_name,
            category,
            brand,
            model,
            status,
            employee_id
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        asset_id,
        asset_name,
        category,
        brand,
        model,
        status,
        employee_id
    ))

    conn.commit()

    cur.close()
    conn.close()


# ==========================
# Get Asset By ID
# ==========================
def get_asset_by_id(asset_id):

    conn = get_connection()
    cur = conn.cursor()

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
        WHERE asset_id=%s
    """, (asset_id,))

    asset = cur.fetchone()

    cur.close()
    conn.close()

    return asset


# ==========================
# Update Asset
# ==========================
def update_asset(asset_id,
                 asset_name,
                 category,
                 brand,
                 model,
                 status,
                 employee_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE asset
        SET
            asset_name=%s,
            category=%s,
            brand=%s,
            model=%s,
            status=%s,
            employee_id=%s
        WHERE asset_id=%s
    """,
    (
        asset_name,
        category,
        brand,
        model,
        status,
        employee_id,
        asset_id
    ))

    conn.commit()

    cur.close()
    conn.close()


# ==========================
# Delete Asset
# ==========================
def delete_asset(asset_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM asset WHERE asset_id=%s",
        (asset_id,)
    )

    conn.commit()

    cur.close()
    conn.close()


# ==========================
# Search Assets
# ==========================
def search_assets(keyword):

    conn = get_connection()
    cur = conn.cursor()

    search = "%" + keyword + "%"

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
        WHERE
            CAST(asset_id AS TEXT) ILIKE %s OR
            asset_name ILIKE %s OR
            category ILIKE %s OR
            brand ILIKE %s OR
            model ILIKE %s OR
            status ILIKE %s OR
            CAST(employee_id AS TEXT) ILIKE %s
        ORDER BY asset_id;
    """,
    (
        search,
        search,
        search,
        search,
        search,
        search,
        search
    ))

    assets = cur.fetchall()

    cur.close()
    conn.close()

    return assets

# ==========================
# Get Assets By Employee
# ==========================
def get_assets_by_employee(employee_id):

    conn = get_connection()
    cur = conn.cursor()

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
        WHERE employee_id=%s
        ORDER BY asset_id;
    """, (employee_id,))

    assets = cur.fetchall()

    cur.close()
    conn.close()

    return assets

def get_employee_asset_list(employee_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            asset_id,
            asset_name
        FROM asset
        WHERE employee_id=%s
        ORDER BY asset_name
    """, (employee_id,))

    assets = cur.fetchall()
    print("Assets Found:", assets)
    cur.close()
    conn.close()

    return assets