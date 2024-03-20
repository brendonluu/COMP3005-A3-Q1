# library used for interacting with PostgreSQL databases from Python
import psycopg2
from psycopg2 import sql

# Database connection parameters
conn_params = {
    "dbname": "school",
    "user": "brendonluu",
    "password": "30925758",
    "host": "localhost"
}

# Decorator function for managing database connections
def db_connect(func):
    # Establish a database connection using the connection parameters
    def wrapper(*args, **kwargs):
        with psycopg2.connect(**conn_params) as conn: # The 'with' statement makes sure the connection is closed automatically after use
            with conn.cursor() as cur: # Create a cursor object to execute SQL commands
                result = func(cur, *args, **kwargs)
                conn.commit()  # Make sure to commit so changes are saved
                return result
    return wrapper

# Retrieves and prints all student records from the 'students' table.
@db_connect
def getAllStudents(cur):
    cur.execute("SELECT * FROM students;")
    records = cur.fetchall()
    for record in records:
        print(record)
    return records  # Return the list of student records 

# Inserts a new student record into the 'students' table
@db_connect
def addStudent(cur, first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date))
    print(f"Student {first_name} {last_name} added successfully.")

# Updates the email address for a student with the specified student_id
@db_connect
def updateStudentEmail(cur, student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id))
    print(f"Student ID {student_id} email updated successfully to {new_email}.")

# Deletes the record of the student with the specified student_id
@db_connect
def deleteStudent(cur, student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    print(f"Student ID {student_id} deleted successfully.")

# Example usage
if __name__ == "__main__":

    print("Initial students:")
    getAllStudents()
    print()

    # print("\nAdding a new student...")
    # addStudent('Brendon', 'Luu', 'brendon.luu@example.com', '2003-09-03')
    # addStudent('Brasdon', 'Lasduu', 'brendon.luasdu@example.com', '2003-09-03')    
    # addStudent('Brenasddon', 'Lasduu', 'brendonasd.luu@example.com', '2003-09-03')

    print("\nDeleting a student...")
    deleteStudent(23)
    deleteStudent(24)
    deleteStudent(25)

    # print("\nUpdating student email...")
    # updateStudentEmail(3, 'NEW.jim.beam@example.com')

    print()
    print("New Students:")
    getAllStudents()

