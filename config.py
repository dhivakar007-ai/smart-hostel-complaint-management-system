import os


class Config:

    # Flask Secret Key
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "smart-hostel-secret-key-2026"
    )


    # Database Configuration

    DATABASE = os.path.join(

        os.path.dirname(__file__),

        "database",

        "app.db"

    )


    # Application Settings

    DEBUG = True


    # Upload Configuration

    UPLOAD_FOLDER = os.path.join(

        "static",

        "uploads"

    )


    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


    # Allowed Upload Types

    ALLOWED_EXTENSIONS = {

        "png",

        "jpg",

        "jpeg",

        "webp"

    }



def allowed_file(filename):

    return (

        "." in filename

        and

        filename.rsplit(".",1)[1].lower()

        in Config.ALLOWED_EXTENSIONS

    )