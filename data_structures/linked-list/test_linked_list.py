import linked_list
import ll_merge.py
import pytest


@pytest.fixture
def empty_list():
    return linked_list.LinkedList()


@pytest.fixture
def int_list():
    return linked_list.LinkedList([1, 2, 3, 4])


@pytest.fixture
def string_list():
    return linked_list.LinkedList(['1', '2', '3', '4'])


def test_insert(empty_list):
    empty_list.insert(1)
    assert empty_list.head.val == 1


def test_find(int_list):
    assert int_list.find(1) is True


def test_string(string_list):
    assert string_list.head.val == '1'


def test_append(int_list):
    assert int_list.append(5) == [1, 2, 3, 4, 5]


def test_before(int_list):
    assert int_list.insert_before(3, 5) == [1, 2, 5, 3, 4]


def test_after(int_list):
    assert int_list.insert_after(3, 5) == [1, 2, 3, 5, 4]


def test_kth(int_list):
    assert int_list.kth_from_end(2).val == 2

def text_merge(int_list, string_list):
    assert ll_merge.merge_lists(int_list, string_list).val == 1
