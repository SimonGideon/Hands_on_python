from databaseCon import test_connection
def sendToCsv():
    conn = test_connection()
    cur = conn.cursor()
    try:
        sql = "COPY (SELECT * FROM datacamp_courses) TO STDOUT WITH CSV DELIMITER ','"
        try:
            with open('datacamp_courses.csv', 'w') as f:
                cur.copy_expert(sql, f)
            print("Data exported to CSV")
        except Exception as e:
            print(f"Error: {e}")
       
    except Exception as e:
        print(f"Error: {e}")
    cur.close()
    conn.close()
sendToCsv()