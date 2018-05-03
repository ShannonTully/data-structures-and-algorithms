"""Tests for left join."""

from .hash_table import HashTable
from .left_join import left_join


def test_basic_input():
    """Test for 2 hash maps with basic buckets."""
    hm1 = HashTable(1)
    hm2 = HashTable(1)
    hm1.set('a', 'bcd')
    hm2.set('a', 'xyz')
    assert left_join(hm1, hm2) == [[1, 'abc', 'xyz']]
