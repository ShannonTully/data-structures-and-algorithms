"""The tests for the selection sorting algorithm."""

from .selection import selection


def test_basic_selection():
    """Basic selection test."""
    unsorted = [2, 1]
    assert selection(unsorted) == [1, 2]


def test_one_element():
    """One element selection test."""
    unsorted = [1]
    assert selection(unsorted) == [1]


def test_less_basic_selection():
    """Less basic selection test."""
    unsorted = [2, 4, 3, 1]
    assert selection(unsorted) == [1, 2, 3, 4]


def test_reversed_selection():
    """Basic reversed order selection test."""
    unsorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert selection(unsorted) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_complex_selection():
    """Complex selection test."""
    unsorted = [49, 682, -9000, 62, 8473, -47, 1]
    assert selection(unsorted) == [-9000, -47, 1, 49, 62, 682, 8473]
