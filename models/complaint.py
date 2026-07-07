from database.database import get_db


class Complaint:

    @staticmethod
    def create(student_id, title, category, description,
               priority="Medium", image=None):

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO complaints
            (
                student_id,
                title,
                category,
                description,
                priority,
                image
            )
            VALUES
            (?, ?, ?, ?, ?, ?)
        """, (
            student_id,
            title,
            category,
            description,
            priority,
            image
        ))

        conn.commit()

        conn.close()

    @staticmethod
    def get_all():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT

                complaints.*,

                students.name AS student_name,

                students.room_number

            FROM complaints

            JOIN students

            ON complaints.student_id = students.id

            ORDER BY complaints.created_at DESC

        """)

        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def get_by_student(student_id):

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT *

            FROM complaints

            WHERE student_id=?

            ORDER BY created_at DESC

        """, (student_id,))

        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def get(id):

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT *

            FROM complaints

            WHERE id=?

        """, (id,))

        data = cursor.fetchone()

        conn.close()

        return data

    @staticmethod
    def update_status(id, status):

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            UPDATE complaints

            SET

            status=?,

            updated_at=CURRENT_TIMESTAMP

            WHERE id=?

        """, (status, id))

        conn.commit()

        conn.close()

    @staticmethod
    def delete(id):

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            DELETE FROM complaints

            WHERE id=?

        """, (id,))

        conn.commit()

        conn.close()

    @staticmethod
    def total():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT COUNT(*)

            FROM complaints

        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def pending():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT COUNT(*)

            FROM complaints

            WHERE status='Pending'

        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def progress():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT COUNT(*)

            FROM complaints

            WHERE status='In Progress'

        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def resolved():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT COUNT(*)

            FROM complaints

            WHERE status='Resolved'

        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def category_report():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT

                category,

                COUNT(*) AS total

            FROM complaints

            GROUP BY category

            ORDER BY total DESC

        """)

        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def monthly_report():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT

                strftime('%m',created_at) AS month,

                COUNT(*) AS total

            FROM complaints

            GROUP BY month

            ORDER BY month

        """)

        data = cursor.fetchall()

        conn.close()

        return data