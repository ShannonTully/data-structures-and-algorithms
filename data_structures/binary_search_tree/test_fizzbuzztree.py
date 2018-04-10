from .fizzbuzztree import FizzBuzzTree as fizz
import pytest


def test_empty_tree(empty_tree):
    assert fizz(empty_tree) is False


def test_fizzbuzztree(fizzbuzz_tree):
    fizz(fizzbuzz_tree)
    assert fizzbuzz_tree.root.val == "fizzbuzz"


def test_no_fizzbuzz(basic_tree):
    fizz(basic_tree)
    assert basic_tree.root.val == 1