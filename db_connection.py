from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', database='postgres', password='tvk7447')
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
