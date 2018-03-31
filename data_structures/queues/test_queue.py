from .queue import Queue
import pytest


def test_empty_queue_has_no_front(empty_queue):
    assert empty_queue.front is None


def test_insertion(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.enqueue(1).val == 1


def test_empty_val_on_insert(empty_queue):
    with pytest.raises(TypeError):
        empty_queue.enqueue()


def test_dequeue_gets_front():
    assert small_queue.dequeue() == 5


def test_len():
    assert len(small_queue) == 4
