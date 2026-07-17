# tests/test_summarize.py

from arxiv_digest.summarize import summarize_papers
from tests.fixtures.sample_data import mock_papers

def test_summarize_papers():

    mock = mock_papers()
    result = summarize_papers(mock)

    assert type(result) == list
    assert hasattr(result[0], "ai_summary")
