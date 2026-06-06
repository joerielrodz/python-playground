import sqlite3


def connect_db():
    return sqlite3.connect("students.db")


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        major TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_student():
    name = input("Enter student name: ")
    major = input("Enter major: ")

    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("Year must be a number.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, major, year) VALUES (?, ?, ?)",
        (name, major, year)
    )

    conn.commit()
    conn.close()

    print("Student added successfully!")


def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    if not students:
        print("No students found.")
    else:
        for student in students:
            print("ID:", student[0], "| Name:", student[1],
                  "| Major:", student[2], "| Year:", student[3])


def menu():
    create_table()

    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


menu()
