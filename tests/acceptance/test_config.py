from pathlib import Path
import pytest
from config import settings


@pytest.mark.acceptance
def test_config():
    assert len(settings.api_key) > 5
    assert isinstance(settings.project_path, Path)
    assert len(settings.project_path.name) > 5
    assert len(settings.model_name) > 5
