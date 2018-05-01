"""Test for repeated words function."""

from .repeated_words import repeated_words


def test_basic_repeat():
    """Test with basic string."""
    assert repeated_words('word word') == 'word'


def test_empty_string():
    """Test empty string."""
    assert repeated_words('') is None


def test_complex_string():
    """Test with a more complex string."""
    complex_string = 'this is a more complex string that has more words in it'
    assert repeated_words(complex_string) == 'more'
