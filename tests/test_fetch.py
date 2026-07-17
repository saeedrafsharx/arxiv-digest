# tests/test_fetch.py
from arxiv_digest.fetch import fetch

def test_fetch():

    query = "nicotine" # not that I abuse it...

    result = fetch(query)
    assert len(result) != 0
    assert type(result) == str