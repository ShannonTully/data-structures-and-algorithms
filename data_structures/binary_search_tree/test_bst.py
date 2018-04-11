from .bst import BST
import pytest


def test_insert(empty_tree):
    assert empty_tree.insert(1) == empty_tree.root


def test_iter_insert(basic_tree):
    assert basic_tree.root.right.right.right.val == 4


def test_in_order(random_tree):
    l = []
    random_tree.in_order(l.append)
    assert l[0].val < l[-1].val


def test_pre_order(random_tree):
    preorder = []
    random_tree.pre_order(preorder.append)
    assert preorder[0].val > preorder[100].val
    assert preorder[0].val < preorder[-1].val


def test_post_order(random_tree):
    postorder = []
    random_tree.post_order(postorder.append)
    assert postorder[-1].val > postorder[0].val
    assert postorder[-1].val < postorder[-2].val


def test_valid_breadth(bigger_tree):
    bread = []
    bigger_tree.breadth_first_traversal(bread.append)
    assert bread[0].val > bread[1].val
    assert bread[0].val < bread[2].val


def test_empty_breadth(empty_tree):
    assert empty_tree.breadth_first_traversal(print) is False


def test_random_breadth(random_tree):
    bread = []
    random_tree.breadth_first_traversal(bread.append)
    assert bread[0].val > bread[1].val
    assert bread[0].val < bread[-1].val
