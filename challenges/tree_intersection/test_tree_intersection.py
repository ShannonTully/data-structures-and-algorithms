"""Tests for tree intersection."""

from data_structures.binary_search_tree.bst import BST
from .tree_intersection import tree_intersection


def test_basic_match_BST():
    """Test that trees that have one val and match return set with val."""
    BST1 = BST([1])
    BST2 = BST([1])

    assert tree_intersection(BST1, BST2) == {1}


def test_basic_no_match_BST():
    """Test that trees that have one val and dont match return nothing."""
    BST1 = BST([1])
    BST2 = BST([2])

    assert tree_intersection(BST1, BST2) is None


def test_big_match_BST():
    """Test that trees that have many val and match return set with vals."""
    BST1 = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    BST2 = BST([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    assert tree_intersection(BST1, BST2) == {2, 4, 6, 8, 10}
