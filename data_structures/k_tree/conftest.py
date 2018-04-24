from .k_tree import KTree
import pytest
from random import randint


@pytest.fixture
def basic_tree():
    return KTree(1)
