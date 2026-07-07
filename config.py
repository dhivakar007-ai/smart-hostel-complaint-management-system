import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret")
    DATABASE = os.environ.get(
        "DATABASE_PATH",
        os.path.join(basedir, "database", "app.db"),
    )
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = 86400
