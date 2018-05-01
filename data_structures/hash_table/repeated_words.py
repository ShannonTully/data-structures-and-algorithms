"""A function that uses a hash table to find the repeated words in a string."""

from .hash_table import HashTable


def repeated_words(string):
    """Find the repeated word."""
    words = string.split(' ')
    ht = HashTable()
    for word in words:
        is_in = ht.get(word)
        if is_in:
            return word
        ht.set(word, word)
