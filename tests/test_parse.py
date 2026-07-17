# tests/test_parse.py

from arxiv_digest.parse import parse_xml
from pathlib import Path

def test_parse_xml():

    xml = Path("tests/fixtures/arxiv_response.xml").read_text()

    result = parse_xml(xml)
    
    assert len(result) != 0
    assert type(result) == list
    assert result[0].title != None
