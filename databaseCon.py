import psycopg2
from psycopg2 import OperationalError


def test_connection():
    try:
        conn = psycopg2.connect(database="datacamp_courses",
                                user="",
                                password="",
                                host="localhost",
                                port="5432")
        print("Connection to PostgreSQL successful")
    except OperationalError as e:
        print(f"Unable to connect to PostgreSQL: {e}")
     # opeining cursor to perform databse operations
    cur = conn.cursor()
    # executing to create tables
    cur.execute("""CREATE TABLE datacamp_courses(
                    course_id SERIAL PRIMARY KEY,
                    course_name VARCHAR(50) UNIQUE NOT NULL,
                    course_instructor VARCHAR(100) NOT NULL,
                    topic VARCHAR(20) NOT NULL
        );""")


    cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to SQL','Izzy Weber','Julia')");
    cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Analyzing Survey Data in Python','EbunOluwa Andrew','Python')");

    cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to ChatGPT','James Chapman','Theory')");

    cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to Statistics in R','Maggie Matsui','R')");

    cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Hypothesis Testing in Python','James Chapman','Python')");

    # persisting the changes
    conn.commit()
    print("Tabel created!")
    cur.close()
    conn.close()


if __name__ == "__main__":
    test_connection()
