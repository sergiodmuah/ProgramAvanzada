from typing import List

class User:
    def __init__(self, name: str, user_id: str):
        self._name = name
        self._user_id = user_id
        self._borrowed_books: List[str] = []  # Lista de ISBNs de los libros prestados

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, value: str) -> None:
        self._user_id = value

    @property
    def borrowed_books(self) -> List[str]:
        return self._borrowed_books

    @borrowed_books.setter
    def borrowed_books(self, value: List[str]) -> None:
        self._borrowed_books = value

    def __str__(self) -> str:
        return f"User: {self._name}, ID: {self._user_id}, Borrowed Books: {', '.join(self._borrowed_books) if self._borrowed_books else 'None'}"
