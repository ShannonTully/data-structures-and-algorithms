from .queue import Queue
from .fifo_animal_shelter import Queue as animal_q
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


@pytest.fixture
def animal_queue():
    return animal_q(['cat', 'dog', 'cat', 'dog'])
