import pymysql
from pymysql.cursors import DictCursor

from config import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DB
)


class Database:

    def __init__(self):

        self.connection = None

    # -------------------------
    # Connect Database
    # -------------------------

    def connect(self):

        if self.connection is None:

            self.connection = pymysql.connect(

                host=MYSQL_HOST,

                user=MYSQL_USER,

                password=MYSQL_PASSWORD,

                database=MYSQL_DB,

                cursorclass=DictCursor,

                autocommit=True

            )

        return self.connection

    # -------------------------
    # Execute SELECT Query
    # -------------------------

    def fetch(self, query, values=None):

        connection = self.connect()

        with connection.cursor() as cursor:

            cursor.execute(query, values)

            return cursor.fetchall()

    # -------------------------
    # Execute SELECT ONE
    # -------------------------

    def fetch_one(self, query, values=None):

        connection = self.connect()

        with connection.cursor() as cursor:

            cursor.execute(query, values)

            return cursor.fetchone()

    # -------------------------
    # INSERT
    # UPDATE
    # DELETE
    # -------------------------

    def execute(self, query, values=None):

        connection = self.connect()

        with connection.cursor() as cursor:

            cursor.execute(query, values)

            connection.commit()

            return cursor.lastrowid

    # -------------------------
    # Close Connection
    # -------------------------

    def close(self):

        if self.connection:

            self.connection.close()

            self.connection = None


db = Database()