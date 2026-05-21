"""A small library management project using classes."""

from __future__ import annotations


class Book:
    """Store basic book information."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self) -> None:
        """Mark the book as borrowed."""

        if self.is_borrowed:
            raise ValueError("book is already borrowed")
        self.is_borrowed = True

    def return_book(self) -> None:
        """Mark the book as available again."""

        self.is_borrowed = False


class Library:
    """Manage a small collection of books."""

    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_available_books(self) -> list[str]:
        return [book.title for book in self.books if not book.is_borrowed]

    def borrow_book(self, title: str) -> str:
        for book in self.books:
            if book.title == title:
                book.borrow()
                return f"You borrowed {book.title}."
        raise ValueError("book not found")


def main() -> None:
    """Run the library project."""

    library = Library()
    library.add_book(Book("Python 101", "Guido Example"))
    library.add_book(Book("Machine Learning Basics", "A. Teacher"))

    print("Available:", library.list_available_books())
    print(library.borrow_book("Python 101"))
    print("Available after borrow:", library.list_available_books())


if __name__ == "__main__":
    main()