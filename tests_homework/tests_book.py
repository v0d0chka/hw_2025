import pytest
import uuid

from models_homework import Book

def test_create_book():
    book = Book(author="Author", title="Book")
    assert book.author == "Author"
    assert book.title == "Book"
    assert book.title[0].upper() == 'B'
    assert len(str(book.id)) == 36

def test_add_book_to_library(sample_library, sample_book):
    sample_library.add_book(sample_book)
    assert len(sample_library.books) == 1
    assert sample_library.books[0] == sample_book

def test_remove_book_from_library(sample_library, sample_book):
    sample_library.add_book(sample_book)
    sample_library.remove_book(sample_book.id)
    assert len(sample_library.books) == 0

def test_get_book_by_id(sample_library, sample_book):
    sample_library.add_book(sample_book)
    book = sample_library.get_book(sample_book.id)
    assert book == sample_book

def test_remove_missing_book(sample_library):
    missing_id = uuid.uuid4()
    sample_library.remove_book(missing_id)
    assert len(sample_library.books) == 0

def test_get_missing_book(sample_library):
    missing_id = uuid.uuid4()
    book = sample_library.get_book(missing_id)
    assert book == {}