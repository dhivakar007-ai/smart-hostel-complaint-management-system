import sqlite3
import os

DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "app.db"
)

def get_db():
    conn = sqlite3.connect(
        DATABASE_PATH
    )
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # Only initialize if the database doesn't exist
    if os.path.exists(DATABASE_PATH):
        return

    conn = get_db()
    cursor = conn.cursor()

    schema_path = os.path.join(
        os.path.dirname(__file__),
        "schema.sql"
    )

    with open(schema_path, "r") as file:
        schema = file.read()

    cursor.executescript(schema)

    conn.commit()
    conn.close()


def query_db(query, args=(), one=False):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        query,
        args
    )

    result = cursor.fetchall()

    conn.close()

    if one:
        return result[0] if result else None

    return result


def execute_db(query, args=()):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        query,
        args
    )

    conn.commit()

    last_id = cursor.lastrowid

    conn.close()

    return last_id