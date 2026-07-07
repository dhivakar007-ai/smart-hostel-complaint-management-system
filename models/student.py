from database.database import get_db


class Student:

    @staticmethod
    def create(name, email, username, password, room_number="", phone=""):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO students
            (
                name,
                email,
                username,
                password,
                room_number,
                phone
            )
            VALUES
            (?, ?, ?, ?, ?, ?)
        """, (
            name,
            email,
            username,
            password,
            room_number,
            phone
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def login(username, password):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM students
            WHERE username=?
            AND password=?
        """, (
            username,
            password
        ))

        student = cursor.fetchone()

        conn.close()

        return student

    @staticmethod
    def get(id):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM students
            WHERE id=?
        """, (id,))

        student = cursor.fetchone()

        conn.close()

        return student

    @staticmethod
    def get_by_username(username):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM students
            WHERE username=?
        """, (username,))

        student = cursor.fetchone()

        conn.close()

        return student

    @staticmethod
    def get_all():

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM students
            ORDER BY id DESC
        """)

        students = cursor.fetchall()

        conn.close()

        return students

    @staticmethod
    def update(id, name, email, room_number, phone):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE students

            SET
                name=?,
                email=?,
                room_number=?,
                phone=?

            WHERE id=?
        """, (
            name,
            email,
            room_number,
            phone,
            id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM students
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
            FROM students
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def complaint_count(student_id):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM complaints
            WHERE student_id=?
        """, (student_id,))

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def resolved_count(student_id):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM complaints
            WHERE student_id=?
            AND status='Resolved'
        """, (student_id,))

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def pending_count(student_id):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM complaints
            WHERE student_id=?
            AND status='Pending'
        """, (student_id,))

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def progress_count(student_id):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM complaints
            WHERE student_id=?
            AND status='In Progress'
        """, (student_id,))

        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def search(keyword):

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM students

            WHERE
                name LIKE ?
                OR username LIKE ?
                OR email LIKE ?
                OR room_number LIKE ?

            ORDER BY name
        """, (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        students = cursor.fetchall()

        conn.close()

        return students