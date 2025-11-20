'''Project: Library Management System 
Author: [Shruti Soumya]
Date: November 19, 2025'''
# Dictionary to store books
books = {}
# Dictionary to store borrowed books
borrowed = {}
import csv
# FUNCTION: Add Books
def add_book():
    print("\nAdd New Book")
    book_id = input("Enter Book ID (e.g., B101): ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter No. of Copies: "))
    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }
    print(f"\nBook '{title}' added successfully!\n")
# FUNCTION: View Books
def view_books():
    print("\nBook List")
    print("ID\tTitle\t\tAuthor\t\tCopies")
    for book_id, data in books.items():
        print(f"{book_id}\t{data['title']}\t{data['author']}\t{data['copies']}")
# FUNCTION: Search Book
def search_book():
    print("\nSearch Book")
    print("1. Search by Book ID")
    print("2. Search by Title\n")
    choice = input("Enter option: ")
    if choice == "1":
        book_id = input("Enter Book ID: ")
        if book_id in books:
            b = books[book_id]
            print(f"\nBook Found!\nTitle: {b['title']} | Author: {b['author']} | Copies: {b['copies']}\n")
        else:
            print("\nBook Not Found!\n")
    elif choice == "2":
        title_part = input("Enter part of the title: ").lower()
        found = False
        for book_id, data in books.items():
            if title_part in data['title'].lower():
                print(f"\nBook Found: {book_id} - {data['title']} - {data['author']} - Copies: {data['copies']}")
                found = True
        if not found:
            print("\nNo matching books found!\n")
    else:
        print("\nInvalid option!\n")
# FUNCTION: Borrow Book
def borrow_book():
    print("\nBorrow a Book")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if book_id in books:
        if books[book_id]['copies'] > 0:
            books[book_id]['copies'] -= 1
            borrowed[student] = book_id
            print(f"\n{student} successfully borrowed {book_id}!\n")
        else:
            print("\nNo copies available!\n")
    else:
        print("\nBook ID does not exist!\n")
# FUNCTION: Return Book
def return_book():
    print("\nReturn a Book")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID to return: ")

    if student in borrowed and borrowed[student] == book_id:
        books[book_id]['copies'] += 1
        del borrowed[student]
        print("\nBook Returned Successfully!\n")
    else:
        print("\nNo matching borrowing record found!\n")

    # List Comprehension to display borrowed list
    borrowed_list = [f"{stud} -> {bk}" for stud, bk in borrowed.items()]

    print("Current Borrowed Books:")
    print(borrowed_list, "\n")
def save_books_to_csv():
    with open("books.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["BookID", "Title", "Author", "Copies"])

        for book_id, data in books.items():
            writer.writerow([book_id, data["title"], data["author"], data["copies"]])

    print("\nBooks saved to books.csv\n")
def load_books_from_csv():
    try:
        with open("books.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books[row["BookID"]] = {
                    "title": row["Title"],
                    "author": row["Author"],
                    "copies": int(row["Copies"])
                }

        print("Books loaded from books.csv\n")

    except FileNotFoundError:
        print("books.csv not found. Using default books.\n")
def save_borrowed_to_csv():
    with open("borrowed.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["StudentName", "BookID"])

        for student, book in borrowed.items():
            writer.writerow([student, book])

    print("Borrowed records saved to borrowed.csv\n")
def load_borrowed_from_csv():
    try:
        with open("borrowed.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                borrowed[row["StudentName"]] = row["BookID"]

        print("Borrowed data loaded from borrowed.csv\n")

    except FileNotFoundError:
        print("borrowed.csv not found. Starting fresh.\n")
# Pre-load 5 books (Requirement)
books = {
    "B101": {"title": "Python Basics", "author": "Guido", "copies": 5},
    "B102": {"title": "DSA", "author": "Cormen", "copies": 3},
    "B103": {"title": "AI Intro", "author": "Russell", "copies": 4},
    "B104": {"title": "Data Science", "author": "Joel", "copies": 2},
    "B105": {"title": "Java Made Easy", "author": "James", "copies": 6}
}
# Load data from CSV if exists
load_books_from_csv()
load_borrowed_from_csv()

while True:
    print("\nLIBRARY MANAGER")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    option = input("Enter your choice: ")

    if option == "1":
        add_book()
    elif option == "2":
        view_books()
    elif option == "3":
        search_book()
    elif option == "4":
        borrow_book()
    elif option == "5":
        return_book()
    elif option == "6":
        save_books_to_csv()
        save_borrowed_to_csv()
        print("\nExiting Program.Thank You!\n")
        break
    else:
        print("\nInvalid choice! Please try again.\n")        