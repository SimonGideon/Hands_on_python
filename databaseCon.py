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
    return conn


if __name__ == "__main__":
    test_connection()
