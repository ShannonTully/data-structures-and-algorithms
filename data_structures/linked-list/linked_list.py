import node


class LinkedList:
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._size = 0
        for item in reversed(iter):
            self.insert(item)

    def __len__(self):
        return self._size

    def __str__(self):
        return 'Linked List with a length of {} nodes where the head node is {}.'.format(len(self), self.head)

    def insert(self, val):
        self._size += 1
        self.head = node.Node(val, self.head)

    def find(self, val):
        current = self.head
        while current:
            if val == current.val:
                return True
            current = current._next
        return False
