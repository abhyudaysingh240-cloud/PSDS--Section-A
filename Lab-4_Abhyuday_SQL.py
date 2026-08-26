import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="tiger"
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")

cursor.execute("CREATE DATABASE IF NOT EXISTS LibraryDB")
cursor.execute("USE LibraryDB")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    department VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    book_title VARCHAR(150) NOT NULL,
    author VARCHAR(100),
    price DECIMAL(10,2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Borrowing (
    borrow_id INT PRIMARY KEY,
    student_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
)
""")

cursor.execute("""
INSERT IGNORE INTO Students
VALUES
(1, 'Abhyuday', 'abhyuday@gmail.com', 'Computer Science'),
(2, 'Rahul', 'rahul@gmail.com', 'Information Technology'),
(3, 'Priya', 'priya@gmail.com', 'Computer Science')
""")

cursor.execute("""
INSERT IGNORE INTO Books
VALUES
(101, 'Database Management Systems', 'Raghu Ramakrishnan', 550.00),
(102, 'Introduction to Algorithms', 'Thomas Cormen', 750.00),
(103, 'Python Programming', 'Mark Lutz', 600.00)
""")

cursor.execute("""
INSERT IGNORE INTO Borrowing
VALUES
(1, 1, 101, '2026-08-26', NULL),
(2, 2, 102, '2026-08-26', NULL),
(3, 3, 103, '2026-08-26', NULL)
""")

connection.commit()

cursor.execute("SELECT * FROM Students")
print("\nStudents:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Books")
print("\nBooks:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Borrowing")
print("\nBorrowing:")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()

print("\nConnection closed.")