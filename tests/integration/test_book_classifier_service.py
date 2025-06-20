from pathlib import PosixPath
from config import settings
from factory import create_book_repository
from infra.model_protocol import FakeModel
from service.book_classifier_service import BookClassifierService


def test_to_prompt():
    service = BookClassifierService(
        FakeModel(), create_book_repository(settings.fixtures_path)
    )

    current = service.to_prompt([PosixPath("hola"), PosixPath("ciao")])

    assert (
        current
        == "From this list of books, I want you to give me a main topic of each one so I can classify them in folders. This is the list: hola, ciao"
    )
