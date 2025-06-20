from pathlib import Path


class BookRepository:
    def __init__(self, path: Path, extensions=("pdf", "epub")):
        self.path = path
        self.extensions: tuple[str, ...] = tuple(
            f".{ext.lower()}" for ext in extensions
        )

    def get_books(self) -> list[Path]:
        return [x for x in self.path.iterdir() if x.suffix.lower() in self.extensions]
