from database.database import query_db


class Admin:
    @staticmethod
    def get_by_username(username):
        return query_db(
            "SELECT * FROM users WHERE username = ? AND role = 'admin';",
            (username,),
            one=True,
        )

    @staticmethod
    def get_statistics():
        total_students = query_db(
            "SELECT COUNT(*) AS count FROM users WHERE role = 'student';", one=True
        )["count"]
        total_complaints = query_db(
            "SELECT COUNT(*) AS count FROM complaints;", one=True
        )["count"]
        pending = query_db(
            "SELECT COUNT(*) AS count FROM complaints WHERE status = 'Pending';", one=True
        )["count"]
        resolved = query_db(
            "SELECT COUNT(*) AS count FROM complaints WHERE status = 'Resolved';", one=True
        )["count"]
        return {
            "students": total_students,
            "complaints": total_complaints,
            "pending": pending,
            "resolved": resolved,
        }
