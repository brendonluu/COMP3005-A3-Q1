# Assignment 3 - Q1: Student Database Management System

- Brendon Luu
- 101233289
- March 18, 2024

## Description:

This Python application provides a simple interface for managing student records in a PostgreSQL database.
It supports basic CRUD (Create, Read, Update, Delete) operations, allowing users to:

- add new student records
- retrieve all student records
- update student email addresses
- delete student records

## Functionality:

- getAllStudents(): Retrieves and displays all student records from the database.
- addStudent(first_name, last_name, email, enrollment_date): Adds a new student record to the database.
- updateStudentEmail(student_id, new_email): Updates the email address for a specific student based on their student ID.
- deleteStudent(student_id): Deletes a student record from the database based on their student ID.

## Requirements

- Python3
- PostgreSQL
- psycopg2 library (can be installed through the command: "pip install psycopg2-binary")

## Running the Application

1. Clone the repository or download the source code to your local machine
2. Navigate to the project directory
3. Update the connection parameters in the code to match your PostgreSQL setup (Specifically, the conn_params dictionary with your database name, user, and password)
4. Test any function as needed as shown in the source code
5. Execute the script by running the following command in the terminal: "python3 a3.py"

### Relevant Links

- Demonstrate Video Link: https://www.youtube.com/watch?v=ur6Xn6w5Ieg
- GitHub Repository URL: https://github.com/brendonluu/COMP3005-A3-Q1
