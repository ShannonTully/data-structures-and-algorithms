"""The tests for the merge sorting algorithm."""

from .mergesort import mergesort


def test_basic_mergesort():
    """Basic mergesort test."""
    unsorted = [2, 1]
    assert mergesort(unsorted) == [1, 2]


def test_one_element():
    """One element mergesort test."""
    unsorted = [1]
    assert mergesort(unsorted) == [1]


def test_less_basic_mergesort():
    """Less basic mergesort test."""
    unsorted = [2, 4, 3, 1]
    assert mergesort(unsorted) == [1, 2, 3, 4]


def test_reversed_mergesort():
    """Basic reversed order mergesort test."""
    unsorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert mergesort(unsorted) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_complex_mergesort():
    """Complex mergesort test."""
    unsorted = [49, 682, -9000, 62, 8473, -47, 1]
    assert mergesort(unsorted) == [-9000, -47, 1, 49, 62, 682, 8473]
