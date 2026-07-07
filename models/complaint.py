from database.database import execute_db, query_db


class Complaint:
    @staticmethod
    def create(student_id, title, description):
        return execute_db(
            "INSERT INTO complaints (student_id, title, description) VALUES (?, ?, ?);",
            (student_id, title, description),
        )

    @staticmethod
    def list_for_student(student_id):
        return query_db(
            "SELECT c.*, u.name AS student_name FROM complaints c JOIN users u ON u.id = c.student_id WHERE c.student_id = ? ORDER BY c.created_at DESC;",
            (student_id,),
        )

    @staticmethod
    def list_all():
        return query_db(
            "SELECT c.*, u.name AS student_name FROM complaints c JOIN users u ON u.id = c.student_id ORDER BY c.created_at DESC;"
        )

    @staticmethod
    def get_by_id(complaint_id):
        return query_db(
            "SELECT c.*, u.name AS student_name, u.room_number FROM complaints c JOIN users u ON u.id = c.student_id WHERE c.id = ?;",
            (complaint_id,),
            one=True,
        )

    @staticmethod
    def update_status(complaint_id, status, admin_note):
        return execute_db(
            "UPDATE complaints SET status = ?, admin_note = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?;",
            (status, admin_note, complaint_id),
        )

    @staticmethod
    def summary_by_status():
        return query_db(
            "SELECT status, COUNT(*) AS count FROM complaints GROUP BY status;"
        )
