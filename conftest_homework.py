import pytest

from models_homework import Book, Library

@pytest.fixture
def sample_book():
    return Book(author="Author", title="Book")

@pytest.fixture
def sample_library():
    library = Library(name="Library")
    return library