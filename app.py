from flask import Flask, redirect, url_for

from config import Config
from database.database import init_app
from routes.auth_routes import auth_bp
from routes.student_routes import student_bp
from routes.admin_routes import admin_bp


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(Config)
    init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def home():
        return redirect(url_for("auth.login"))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
