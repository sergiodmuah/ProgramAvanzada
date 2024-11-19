from book import Book
from typing import List

class Library:
    def __init__(self):
        self.books: List[Book] = []  # Lista para almacenar libros

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, isbn: str) -> None:
        self.books = [book for book in self.books if book.isbn != isbn]

    def lend_book(self, isbn: str) -> None:
        for book in self.books:
            if book.isbn == isbn and not book.status:
                book.status = True
                print(f"The book '{book.title}' has been lent.")
                return
        print("Book not available or already lent.")

    def return_book(self, isbn: str) -> None:
        for book in self.books:
            if book.isbn == isbn and book.status:
                book.status = False
                print(f"The book '{book.title}' has been returned.")
                return
        print("Book not found or wasn't lent.")

    def find_books_by_title(self, title: str) -> List[Book]:
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books if author.lower() in book.author.lower()]

    def display_books(self) -> None:
        if not self.books:
            print("No books available in the library.")
        for book in self.books:
            print(book)
