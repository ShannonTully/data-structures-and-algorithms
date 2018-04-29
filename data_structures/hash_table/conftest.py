"""conftest for Hash Table tests."""

from .hash_table import HashTable
import pytest


@pytest.fixture
def empty_hash_table():
    """Empty hash table."""
    return HashTable()


@pytest.fixture
def basic_hash_table():
    """Not empty hash table."""
    return HashTable(1)
