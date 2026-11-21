
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author,
            "available": True
        }

        self.books.append(book)
        print(f"{title} added successfully.")

    def borrow_book(self, title):
        for book in self.books:
            if book["title"] == title:

                # Check if the book is already borrowed
                if not book["available"]:
                    print(f"{title} is already borrowed.")
                    return

                book["available"] = False
                print(f"You borrowed {title}.")
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title:

                if book["available"]:
                    print(f"{title} is already available.")
                    return

                book["available"] = True
                print(f"{title} returned successfully.")
                return

        print("Book not found.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            status = "Available" if book["available"] else "Borrowed"
            print(f'{book["title"]} - {book["author"]} - {status}')


# Create a library
library = Library()

# Add books
library.add_book("Python Basics", "John Smith")
library.add_book("Clean Code", "Robert Martin")

# Borrow books
library.borrow_book("Python Basics")
library.borrow_book("Python Basics")

# Show all books
library.show_books()

