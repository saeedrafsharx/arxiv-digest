# tests/test_cli.py
from arxiv_digest.cli import main
import pytest

def test_cli_model(capsys):

    main(["nicotine"])

    captured = capsys.readouterr()

    assert "Title" in captured.out