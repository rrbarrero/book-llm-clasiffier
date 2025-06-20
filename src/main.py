from pathlib import Path
import typer

from factory import create_book_classifier_service

app = typer.Typer()


@app.command()
def main(path: Path):
    if not path.exists():
        typer.echo(f"Path not found")
        raise typer.Exit(code=1)

    service = create_book_classifier_service(path)
    print(service.classify_books())


if __name__ == "__main__":
    app()
