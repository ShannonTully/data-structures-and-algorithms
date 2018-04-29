"""Hash Table tests."""

from .hash_table import HashTable


def test_hash_table_creation():
    """Test that a Hash Table can be created."""
    table = HashTable(100)
    assert len(table.buckets) == 100


def test_hash_key(empty_hash_table):
    """Test hash works."""
    assert empty_hash_table._hash_key('abc') == 294


def test_set(empty_hash_table):
    """Test set works."""
    empty_hash_table.set('abc', 'a')
    assert empty_hash_table.buckets[294].head.val['abc'] == 'a'


def test_bucket(basic_hash_table):
    """Test bucket works."""
    basic_hash_table.set('abc', 'a')
    basic_hash_table.set('xyz', 'b')
    assert basic_hash_table.buckets[0].head.val['xyz'] == 'b'
    assert basic_hash_table.buckets[0].head._next.val['abc'] == 'a'


def test_get(empty_hash_table):
    """Test get works."""
    empty_hash_table.set('abc', 'a')
    assert empty_hash_table.get('abc') == 'a'


def test_get_from_bucket(basic_hash_table):
    """Test gets the value from a bucket with more than one thing in it."""
    basic_hash_table.set('abc', 'a')
    basic_hash_table.set('xyz', 'b')
    assert basic_hash_table.get('abc') == 'a'
    assert basic_hash_table.get('xyz') == 'b'


def test_get_from_different_buckets(empty_hash_table):
    """Test get works from different buckets."""
    empty_hash_table.set('abc', 'a')
    empty_hash_table.set('xyz', 'b')
    assert empty_hash_table.get('abc') == 'a'
    assert empty_hash_table.get('xyz') == 'b'


def test_remove_nonexisting(empty_hash_table):
    """Test removal of nothing."""
    empty_hash_table.set('abc', 'a')
    empty_hash_table.remove('xyz')
    assert empty_hash_table.get('abc') == 'a'


def test_remove(basic_hash_table):
    """Test removal."""
    basic_hash_table.set('abc', 'a')
    basic_hash_table.set('xyz', 'b')
    basic_hash_table.remove('xyz')
    assert basic_hash_table.get('abc') == 'a'
    assert basic_hash_table.get('xyz') is None


def test_dump(basic_hash_table):
    """Test dump."""
    basic_hash_table.set('abc', 'a')
    basic_hash_table.set('xyz', 'b')
    basic_hash_table.remove('abc', True)
    assert basic_hash_table.get('abc') is None
    assert basic_hash_table.get('xyz') is None
    assert len(basic_hash_table.buckets[0]) == 0
