import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("Select * FROM students")

students = cursor.fetchall()


for student in students:
    if student[1] == "Maria":
        print(student)

conn.close()
