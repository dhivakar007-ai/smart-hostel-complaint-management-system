from database.database import execute_db, query_db
from werkzeug.security import check_password_hash, generate_password_hash


class Student:
    @staticmethod
    def create(username, password, name, email, room_number):
        hashed_password = generate_password_hash(password)
        return execute_db(
            "INSERT INTO users (username, password, name, email, room_number, role) VALUES (?, ?, ?, ?, ?, 'student');",
            (username, hashed_password, name, email, room_number),
        )

    @staticmethod
    def get_by_username(username):
        return query_db(
            "SELECT * FROM users WHERE username = ? AND role = 'student';",
            (username,),
            one=True,
        )

    @staticmethod
    def get_by_id(student_id):
        return query_db(
            "SELECT * FROM users WHERE id = ? AND role = 'student';",
            (student_id,),
            one=True,
        )

    @staticmethod
    def update_profile(student_id, name, email, room_number):
        return execute_db(
            "UPDATE users SET name = ?, email = ?, room_number = ? WHERE id = ? AND role = 'student';",
            (name, email, room_number, student_id),
        )

    @staticmethod
    def check_password(user, password):
        return check_password_hash(user["password"], password)

    @staticmethod
    def list_all():
        return query_db("SELECT * FROM users WHERE role = 'student' ORDER BY name;")

    @staticmethod
    def delete(student_id):
        return execute_db("DELETE FROM users WHERE id = ? AND role = 'student';", (student_id,))
