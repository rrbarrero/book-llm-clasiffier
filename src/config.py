from pydantic import Field
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    api_key: str = Field(..., alias="API_KEY")
    project_path: Path
    model_name: str = Field(
        default="models/gemini-2.5-flash-preview-04-17", alias="MODEL_NAME"
    )

    model_config = {
        "env_file": ".env",
        "populate_by_name": True,
    }

    @classmethod
    def load(cls):
        return cls(project_path=Path(__file__).parent.parent)  # type: ignore

    @property
    def fixtures_path(self) -> Path:
        return self.project_path / "tests" / "__fixtures__"


settings = Settings.load()  # type: ignore
