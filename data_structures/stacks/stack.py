from .node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0
        for item in reversed(iterable):
            self.push(item)

    def __len__(self):
        return self._size

    def __str__(self):
        return self.top

    def push(self, val):
        try:
            node = Node(val)
        except TypeError:
            print('That value is unacceptable.')
            exit()

        node._next = self.top
        self.top = node
        self._size += 1

        return self.top

    def pop(self):
        popped = self.top
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        return self.top
