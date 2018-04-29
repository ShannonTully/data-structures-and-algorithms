"""Hash Table that works off of my premade linked list."""

from ..linked_list.linked_list import LinkedList


class HashTable:
    """Hash Table."""

    def __init__(self, max_size=1024):
        """Hash Table initilization."""
        self.max_size = max_size
        self.buckets = [LinkedList() for _ in range(max_size)]

    def _hash_key(self, val):
        """Get the hashed key."""
        return sum(map(lambda x: ord(x), val)) % self.max_size

    def set(self, key, val):
        """Insert into hash table."""
        return self.buckets[self._hash_key(key)].insert({key: val})

    def get(self, key):
        """Get value."""
        current = self.buckets[self._hash_key(key)].head
        while current:
            if key in current.val.keys():
                return current.val[key]
            current = current._next

    def remove(self, key, dump=False):
        """Remove value or dump bucket."""
        bucket = self.buckets[self._hash_key(key)]
        current = bucket.head
        last = current
        while current:
            if key in current.val.keys():
                if dump:
                    bucket.head = None
                    bucket._size = 0
                else:
                    if last is not current:
                        last._next = current._next
                    else:
                        bucket.head = current._next
                return current.val[key]

            last = current
            current = current._next
