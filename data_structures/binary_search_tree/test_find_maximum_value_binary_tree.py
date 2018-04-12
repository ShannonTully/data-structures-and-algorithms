from .find_maximum_value_binary_tree import find_maximum_value_binary_tree as high
import pytest


def test_empty_tree(empty_tree):
    assert high(empty_tree) is None


def test_fizzbuzztree(basic_tree):
    assert high(basic_tree) == 4


def test_no_fizzbuzz(bigger_tree):
    assert high(bigger_tree) == 28
