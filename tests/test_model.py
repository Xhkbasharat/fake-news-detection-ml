from src.preprocess import clean_text


def test_clean_text_lowercase():
    assert clean_text("BREAKING NEWS") == "breaking news"


def test_clean_text_removes_url():
    assert "https" not in clean_text("Visit https://example.com for news")


def test_clean_text_removes_numbers():
    assert clean_text("News from 2025") == "news from"


def test_clean_text_handles_empty_input():
    assert clean_text("") == ""


def test_clean_text_handles_non_string():
    assert clean_text(None) == ""
