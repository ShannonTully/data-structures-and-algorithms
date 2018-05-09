"""The tests for the quick sorting algorithm."""

from .quicksort import quicksort


def test_basic_quicksort():
    """Basic quicksort test."""
    unsorted = [2, 1]
    assert quicksort(unsorted) == [1, 2]


def test_one_element():
    """One element quicksort test."""
    unsorted = [1]
    assert quicksort(unsorted) == [1]


def test_less_basic_quicksort():
    """Less basic quicksort test."""
    unsorted = [2, 4, 3, 1]
    assert quicksort(unsorted) == [1, 2, 3, 4]


def test_reversed_quicksort():
    """Basic reversed order quicksort test."""
    unsorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert quicksort(unsorted) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_complex_quicksort():
    """Complex quicksort test."""
    unsorted = [49, 682, -9000, 62, 8473, -47, 1]
    assert quicksort(unsorted) == [-9000, -47, 1, 49, 62, 682, 8473]
