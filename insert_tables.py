import logging
import random

from faker import Faker
from psycopg2 import DatabaseError

from db_connection import create_connection


fake = Faker('uk-Ua')
COUNT = 5

def insert_data(conn, sql_expression: str, *args):
    c = conn.cursor()
    try:
        # for _ in range(COUNT):
        c.execute(sql_expression, args)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sgl_insert_students = """
        INSERT INTO students (fullname, group_id) VALUES (%s, %s);
        """
    sgl_insert_groups = """
        INSERT INTO groups_ (name) VALUES (%s);
        """
    sgl_insert_teachers = """
        INSERT INTO teachers (fullname) VALUES (%s);
        """
    sgl_insert_disciplines = """
        INSERT INTO disciplines (name, teacher_id) VALUES (%s, %s);
        """
    sql_insert_grades = """
        INSERT INTO grades (discipline_id, student_id, grade, date_of) VALUES (%s, %s, %s, %s);
        """

    try:
        with create_connection() as conn:
            if conn is not None:
                for _ in range(3):
                    insert_data(conn, sgl_insert_groups, (fake.word(),))
                    insert_data(conn, sgl_insert_teachers, (fake.name(),))
                for teacher_id in range(1, 4):
                    for _ in range(2):
                        insert_data(conn, sgl_insert_disciplines, fake.word(), teacher_id)
                for group_id in range(1, 4):
                    for _ in range(10):
                        insert_data(conn,sgl_insert_students, fake.name(), group_id)
                for discipline_id in range(1, 7):
                    for student_id in range(1, 31):
                        insert_data(conn,sql_insert_grades, discipline_id, student_id, random.randint(0, 100), fake.date_this_decade())
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
