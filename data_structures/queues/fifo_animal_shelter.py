from .node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0
        for item in iterable:
            self.enqueue(item)

    def __len__(self):
        return self._size

    def __str__(self):
        return self.front

    def enqueue(self, val):
        node = Node(val)

        if self._size == 0:
            self.front = self.back = node
            self._size += 1
            return node

        # self.back.next = self.back = node
        
        self.back.next = node
        self.back = node

        self._size += 1
        return node

    def dequeue(self, pref):
        if pref in ('cat', 'dog', None):
            current = self.front
            current1 = None
            if self._size == 0:
                raise IndexError('List is empty')
            elif self.front.val == pref:
                temp = self.front
                self.front = temp.next
                self._size -= 1
                return temp.val
            else:
                while current._next:
                    if current._next.val == pref.lower():
                        current1 = current._next
                        current._next = current._next._next
                        self._size -= 1
                        return current1.val
                    current = current._next
        else:
            print('Not here')
