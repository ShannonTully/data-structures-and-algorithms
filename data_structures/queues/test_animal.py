from .fifo_animal_shelter import Queue
import pytest


def test_dequeue_gets_animal(animal_queue):
    assert animal_queue.dequeue('cat') == 'cat'
