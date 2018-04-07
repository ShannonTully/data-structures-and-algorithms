from .bst import BST
import pytest
from random import randint


@pytest.fixture
def basic_tree():
    return BST([1, 2, 3, 4])


@pytest.fixture
def empty_tree():
    return BST()


@pytest.fixture
def random_tree():
    return BST([randint(0, 100000) for x in range(100000)])


@pytest.fixture
def bigger_tree():
    return BST([20, 15, 12, 18, 25, 28, 22])
