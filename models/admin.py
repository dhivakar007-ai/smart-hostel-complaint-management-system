from database.database import get_db


class Admin:

    @staticmethod
    def login(username, password):

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT *

            FROM admins

            WHERE username=?

            AND password=?

        """, (

            username,

            password

        ))

        admin = cursor.fetchone()

        conn.close()

        return admin

    @staticmethod
    def create(username, password):

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            INSERT INTO admins

            (

                username,

                password

            )

            VALUES

            (?,?)

        """, (

            username,

            password

        ))

        conn.commit()

        conn.close()

    @staticmethod
    def get_all():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT *

            FROM admins

            ORDER BY id

        """)

        admins = cursor.fetchall()

        conn.close()

        return admins

    @staticmethod
    def total():

        conn = get_db()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT COUNT(*)

            FROM admins

        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total