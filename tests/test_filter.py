# tests/test_filter.py
from arxiv_digest.filter import filter_papers, drop_seen
from tests.fixtures.sample_data import mock_papers

def test_filter_papers():

    mock = mock_papers()
    result = filter_papers(mock, keywords="nicotine")

    assert len(result) != 5
    assert type(result) == list
    assert result[0].title != None 

