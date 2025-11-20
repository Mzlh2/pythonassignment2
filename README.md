# pythonassignment2
Library Management System (Python)

This is a beginner-friendly command-line Library Management System written in Python.
It allows the user to add, view, search, borrow, return, save, and load book records.
Project Structure
library_manager/
│
├── library.py
├── books.csv
├── borrowed.csv
└── README.md
Features

Add Books
Enter Book ID, Title, Author, and Number of Copies.

View Books
Displays all books in a clear tabular format.

Search Books

Search by Book ID

Search by Title (substring match)

Borrow Book
Allows a student to borrow a book and reduces the available copies.

Return Book
Increases the number of copies and removes the borrowing record.

Save and Load (CSV)

Automatically loads book and borrowing data from CSV files at program start.

Automatically saves all data to CSV files when the program exits.

Menu-Driven Program
Runs in a loop and allows multiple operations until the user selects Exit.
How to Run the Program
1. Install Python (version 3 or above).
2. Open the terminal or command prompt.
3. Navigate to the project folder using: cd library_manager
4. Run the program: python library.py
CSV Files Used

books.csv
Stores book information in the format:
BookID, Title, Author, Copies

borrowed.csv
Stores borrowing records in the format:
StudentName, BookID

These files are automatically created and updated when exiting the program.
