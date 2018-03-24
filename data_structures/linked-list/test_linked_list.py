import linked_list
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