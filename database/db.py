import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Return a new psycopg2 connection using environment variables.

    Raises a ValueError if required environment variables are missing.
    """
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    port = os.getenv("DB_PORT")

    if not all([host, database, user, password]):
        raise ValueError("Database configuration incomplete. Please set DB_HOST, DB_NAME, DB_USER, and DB_PASSWORD in your environment or .env file.")

    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=int(port) if port else None,
    )

    return conn