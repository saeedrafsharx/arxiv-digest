# tests/test_config.py

from arxiv_digest.config import import_config

def test_import_config():

    config = import_config()
    assert config != None