class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._status = False  # False significa que no está prestado.

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = value

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        self._isbn = value

    @property
    def status(self) -> bool:
        return self._status

    @status.setter
    def status(self, value: bool) -> None:
        self._status = value

    def __str__(self) -> str:
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Status: {'Lent' if self._status else 'Available'}"
