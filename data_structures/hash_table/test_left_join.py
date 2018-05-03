"""Tests for left join."""

from .hash_table import HashTable
from .left_join import left_join


def test_basic_input():
    """Test for 2 hash maps with basic buckets."""
    hm1 = HashTable(1)
    hm2 = HashTable(1)
    hm1.set('a', 'bcd')
    hm2.set('a', 'xyz')
    assert left_join(hm1, hm2) == {'a': ['bcd', 'xyz']}


def test_complex_input():
    """Test with a more complex set of keys and values."""
    hm1 = HashTable()
    hm2 = HashTable()
    hm1.set('abc', 'a')
    hm2.set('abc', 'b')
    hm1.set('bcd', 'c')
    hm2.set('cde', 'd')
    hm1.set('def', 'e')
    hm2.set('def', 'f')
    hm1.set('efg', 'g')
    hm2.set('fgh', 'h')
    hm1.set('fgh', 'i')
    hm2.set('ghi', 'j')
    assert left_join(hm1, hm2) == {'abc': ['a', 'b'], 'bcd': ['c', None], 'def': ['e', 'f'], 'efg': ['g', None], 'fgh': ['i', 'h']}


def test_empty_input():
    """Test for empty hash tables."""
    hm1 = HashTable()
    hm2 = HashTable()
    assert left_join(hm1, hm2) == {}
