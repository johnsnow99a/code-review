
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
                book["available"] = False
                print(f"You borrowed {title}.")
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title:
                book["available"] = True
                print(f"{title} returned successfully.")
                return

        print("Book not found.")

    def show_books(self):
        for book in self.books:
            status = "Available" if book["available"] else "Borrowed"
            print(f'{book["title"]} - {book["author"]} - {status}')


library = Library()

library.add_book("Python Basics", "John Smith")
library.add_book("Clean Code", "Robert Martin")

library.borrow_book("Python Basics")
library.borrow_book("Python Basics")

library.show_books()
