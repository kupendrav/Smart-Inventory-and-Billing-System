# Database connection settings
import os

import psycopg2


def connection():
    config = {
        "host": os.getenv("DB_HOST", "localhost"),
        "database": os.getenv("DB_NAME", "ecommerce"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "1999"),
        "port": os.getenv("DB_PORT", "5432"),
    }

    try:
        con = psycopg2.connect(**config)
        print("Connection successful")
        return con
    except psycopg2.OperationalError as exc:
        raise RuntimeError(
            "PostgreSQL connection failed. Check DB_HOST, DB_NAME, DB_USER, "
            "DB_PASSWORD, and DB_PORT. Original error: "
            f"{exc}"
        ) from exc


conn = connection()
