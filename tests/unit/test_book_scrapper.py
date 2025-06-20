from pathlib import PosixPath
from infra.book_scrapper import BookRepository
from config import settings


def test_book_scrapper():
    repo = BookRepository(settings.fixtures_path)

    books = repo.get_books()

    assert books == [
        PosixPath(f"{settings.fixtures_path}/book1.pdf"),
        PosixPath(f"{settings.fixtures_path}/book2.epub"),
    ]
