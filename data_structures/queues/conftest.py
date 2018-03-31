from .queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    return Queue([1, 2, 3, 4])


@pytest.fixture
def large_queue():
    q = Queue()

    for num in range(1000):
        q.enqueue(num)

    return q
