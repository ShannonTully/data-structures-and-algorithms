from .node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0
        for item in reversed(iterable):
            self.enqueue(item)

    def __len__(self):
        return self._size

    def __str__(self):
        return self.front

    def enqueue(self, val):
        try:
            node = Node(val)
        except TypeError:
            print('That value is unacceptable.')
            exit()

        node._next = self.back
        self.back = node
        self._size += 1

        return self.back

    def dequeue(self):
        new_guy = self.front
        self.front = self.front.next
        self._size -= 1
        return new_guy
