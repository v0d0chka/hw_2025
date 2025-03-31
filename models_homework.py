import uuid
from typing import Self


class Book:
    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title
        self.id = uuid.uuid4()


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_id: uuid.UUID):
        self.books = [book for book in self.books if book.id != book_id]

    def get_book(self, book_id: uuid.UUID) -> Book:
        for book in self.books:
            if book.id == book_id:
                return book