from .k_tree import KTree
from .find_matches import find_matches
import pytest


def test_insert(basic_tree):
    basic_tree.insert(2, basic_tree.root.val)
    assert basic_tree.root.children[0].val == 2


def test_pre_order(basic_tree):
    preorder = []
    basic_tree.insert(2, basic_tree.root.val)
    # import pdb; pdb.set_trace()
    basic_tree.pre_order(preorder.append)
    assert preorder[1].val > preorder[0].val


def test_post_order(basic_tree):
    postorder = []
    basic_tree.insert(2, basic_tree.root.val)
    basic_tree.post_order(postorder.append)
    assert postorder[0].val > postorder[1].val


def test_valid_breadth(basic_tree):
    bread = []
    basic_tree.insert(2, basic_tree.root.val)
    basic_tree.breadth_first_traversal(bread.append)
    assert bread[1].val > bread[0].val


def test_basic_valid_print_level(basic_tree):
    assert basic_tree.print_level_order() == '''1
'''


def test_valid_print_level(basic_tree):
    basic_tree.insert(2, basic_tree.root.val)
    assert basic_tree.print_level_order() == '''1
2
'''


def test_complex_valid_print_level(basic_tree):
    basic_tree.insert(2, basic_tree.root.val)
    basic_tree.insert(3, basic_tree.root.val)
    basic_tree.insert(4, 2)
    basic_tree.insert(5, 2)
    basic_tree.insert(6, 3)
    basic_tree.insert(7, 6)
    assert basic_tree.print_level_order() == '''1
23
456
7
'''


def test_basic_none_find(basic_tree):
    """Test find_matches for a basic k-nary tree where there are no matches."""
    assert find_matches(basic_tree, 2) is False


def test_basic_valid_find(basic_tree):
    """Test find_matches for a basic k-nary tree where there is a match."""
    assert find_matches(basic_tree, 1)[0].val == 1


def test_complex_valid_find(basic_tree):
    """Test find_matches for a complex k-nary tree where there is a match."""
    basic_tree.insert(2, basic_tree.root.val)
    basic_tree.insert(3, basic_tree.root.val)
    basic_tree.insert(3, 2)
    basic_tree.insert(5, 2)
    basic_tree.insert(6, 3)
    basic_tree.insert(3, 6)
    assert find_matches(basic_tree, 3)[0].val == 3
    assert find_matches(basic_tree, 3)[1].val == 3
    assert find_matches(basic_tree, 3)[2].val == 3
