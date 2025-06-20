from config import settings
from pathlib import Path
from infra.book_scrapper import BookRepository
from infra.gemini_model import Gemini
from service.book_classifier_service import BookClassifierService


def create_book_repository(path: Path):
    return BookRepository(path)


def create_gemini_model():
    return Gemini(settings.api_key, settings.model_name)


def create_book_classifier_service(path: Path):
    return BookClassifierService(
        create_gemini_model(),
        create_book_repository(path),
    )
