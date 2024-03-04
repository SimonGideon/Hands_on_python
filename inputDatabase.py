from databaseCon import test_connection
import psycopg2

def input_to_database():
    try:
        conn = test_connection()
        course_name = input("Enter Course Name: ")
        course_instructor = input("Enter Instructor Name: ")
        topic = input("Enter the topic: ")
        cur = conn.cursor()
        # cur.execute(f"INSERT INTO datacamp_courses VALUES(25, '{course_name}', '{course_instructor}', '{topic}')")
        cur.execute("INSERT INTO datacamp_courses (course_name, course_instructor, topic) VALUES (%s, %s, %s)", 
                    (course_name, course_instructor, topic))
        conn.commit()
        print("\nAdding...........")
        print(f"Course Name: {course_name}, \nInstructor Name: {course_instructor}, \nTopic Name: {topic} \n✔ Added successfully!")
        cur.execute("SELECT * FROM datacamp_courses")
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting:", error)

input_to_database()
