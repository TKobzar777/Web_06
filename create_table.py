from db_connection import create_connection

create_table_users = """

DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  password VARCHAR(50),
  age NUMERIC CHECK (age > 0 AND age < 150)
);
"""

create_table_groups = """
DROP TABLE IF EXISTS groups_ CASCADE;
CREATE TABLE groups_ (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50)
  );
"""
create_table_teachers = """
DROP TABLE IF EXISTS teachers CASCADE;
CREATE TABLE teachers (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(50)
);
"""

create_table_students = """
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(50),
  group_id INTEGER REFERENCES groups_ (id)
);
"""

create_table_disciplines = """
DROP TABLE IF EXISTS disciplines CASCADE;
CREATE TABLE disciplines (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  teacher_id INTEGER REFERENCES teachers (id)
);
"""

create_table_grades = """
DROP TABLE IF EXISTS grades CASCADE;
CREATE TABLE grades (
  id SERIAL PRIMARY KEY,
  discipline_id INTEGER REFERENCES disciplines (id),
  student_id INTEGER REFERENCES students (id),
  grade INTEGER,
  date_of DATE
);
"""

if __name__ == '__main__':
    with create_connection() as conn:
        c = conn.cursor()
        c.execute(create_table_groups)
        c.execute(create_table_teachers)
        c.execute(create_table_students)
        c.execute(create_table_disciplines)
        c.execute(create_table_grades)
        c.close()