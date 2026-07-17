# tests/test_store.py

from arxiv_digest.store import save_seen, load_seen
from tests.fixtures.sample_data import mock_papers
import pytest

mock = mock_papers()

def test_save_seen(tmp_path):

    output_file = tmp_path / "test.json"

    result = save_seen(papers=mock, path=output_file)

    assert result is None

    assert output_file.exists()

    content = output_file.read_text()
    assert len(content) != 0

def test_load_seen():
    
    result = load_seen("tests/fixtures/seen.json")

    assert type(result) == list
    assert len(result) != 0