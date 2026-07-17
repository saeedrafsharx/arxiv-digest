# tests/test_render.py

from arxiv_digest.render import render_compact, render_expanded, render_markdown, render_summary
from tests.fixtures.sample_data import mock_papers
import pytest

mock = mock_papers()

def test_render_compact(capsys):

    result = render_compact(mock)

    assert result is None

    captured = capsys.readouterr()
    assert "Title" in captured.out

def test_render_expanded(capsys):

    result = render_expanded(mock)

    assert result is None

    captured = capsys.readouterr()
    assert "Abstract" in captured.out
    print(captured.out)

def test_render_markdown(tmp_path):

    output_file = tmp_path / "test.md"
    result = render_markdown(papers=mock, path=output_file)

    assert result is None
    assert output_file.exists()

    content = output_file.read_text()

    assert "Title" in content

