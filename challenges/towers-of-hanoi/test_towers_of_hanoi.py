import towers_of_hanoi
import pytest


def test_even():
    assert towers_of_hanoi.towers_of_hanoi(2) == 3


def test_odd():
    assert towers_of_hanoi.towers_of_hanoi(3) == 7


def test_huge():
    assert towers_of_hanoi.towers_of_hanoi(10) == 1023
