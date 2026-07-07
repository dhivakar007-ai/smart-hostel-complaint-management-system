import os
import sqlite3
from flask import current_app, g
from werkzeug.security import check_password_hash, generate_password_hash


def get_db():
    if "db" not in g:
        db_path = current_app.config["DATABASE"]
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        g.db = sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def execute_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    return cur.lastrowid


def _table_exists(table_name):
    result = query_db(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
        (table_name,),
        one=True,
    )
    return result is not None


def init_db():
    if _table_exists("users") and _table_exists("complaints"):
        return

    with current_app.open_resource("database/schema.sql") as f:
        get_db().executescript(f.read().decode("utf8"))

    create_default_admin()


def create_default_admin():
    existing = query_db(
        "SELECT id FROM users WHERE username = ?;", ("admin",), one=True
    )
    if existing:
        return

    password = generate_password_hash("admin123")
    execute_db(
        "INSERT INTO users (username, password, name, email, room_number, role) VALUES (?, ?, ?, ?, ?, ?);",
        ("admin", password, "Admin", "admin@example.com", "N/A", "admin"),
    )


def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()
