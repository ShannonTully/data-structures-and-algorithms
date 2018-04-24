from .k_tree import KTree
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
