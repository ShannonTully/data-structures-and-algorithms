from .stack import Stack
import pytest


def test_empty_stack_has_no_top(empty_stack):
    assert empty_stack.top is None


def test_insertion(empty_stack):
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1


def test_empty_val_on_insert(empty_stack):
    with pytest.raises(TypeError):
        empty_stack.push()


def test_pop_gets_top():
    assert other_stack.pop() == 5


def test_peek_gets_top():
    assert other_stack.peek() == 5


def test_len():
    assert len(other_stack) == 4