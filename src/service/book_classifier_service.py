from infra.book_scrapper import BookRepository
from pathlib import Path

from infra.model_protocol import ModelProtocol


class BookClassifierService:
    def __init__(self, model: ModelProtocol, repo: BookRepository):
        self.model = model
        self.repo = repo

    def classify_books(self):
        books = self.repo.get_books()
        prompt = self.to_prompt(books)
        return self.model.answer(prompt)

    def to_prompt(self, books: list[Path]):
        return (
            """From this list of books, I want you to give me a main topic of each one """
            """so I can classify them in folders. This is the list: """
            f"""{", ".join([str(x) for x in books])}"""
        )
