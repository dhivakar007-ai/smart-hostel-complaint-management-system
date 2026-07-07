from flask import Flask

from flask import session

from config import Config

from database.database import init_db


from routes.auth_routes import auth

from routes.student_routes import student

from routes.admin_routes import admin



# ---------------------------------------
# Create Application
# ---------------------------------------

app = Flask(__name__)


app.config.from_object(Config)



# ---------------------------------------
# Database Initialize
# ---------------------------------------

with app.app_context():

    init_db()



# ---------------------------------------
# Register Blueprints
# ---------------------------------------

app.register_blueprint(auth)

app.register_blueprint(student)

app.register_blueprint(admin)



# ---------------------------------------
# Context Processor
# ---------------------------------------

@app.context_processor
def inject_user():

    return {

        "logged_in":

        "username" in session

    }



# ---------------------------------------
# Error Pages
# ---------------------------------------

@app.errorhandler(404)
def page_not_found(error):

    return """

    <div style='
    text-align:center;
    margin-top:100px;
    font-family:Poppins;
    '>

    <h1>404</h1>

    <h2>Page Not Found</h2>

    <a href='/'>Go Home</a>

    </div>

    """,404



@app.errorhandler(500)
def server_error(error):

    return """

    <div style='
    text-align:center;
    margin-top:100px;
    font-family:Poppins;
    '>

    <h1>500</h1>

    <h2>Something went wrong</h2>

    </div>

    """,500



# ---------------------------------------
# Run Application
# ---------------------------------------

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )