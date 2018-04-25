class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = []
        for child in children:
            self.children.append(Node(child))

    def __repr__(self):
        return 'node is {}'.format(str(self.val))

    def __str__(self):
        return str(self.val)


class KTree:
    def __init__(self, val):
        self.root = Node(val)

    def __repr__(self):
        return 'root is {}'.format(str(self.root.val))

    def __str__(self):
        return str(self.root.val)

    def insert(self, val, parent):
        self.breadth_first_traversal(lambda x: x.children.append(Node(val)) if x.val == parent else False)

    def pre_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if len(node.children):
                for child in node.children:
                    _walk(child)

        _walk(self.root)

    def post_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if len(node.children):
                for child in node.children:
                    _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self, operation):
        def _walk(nodes):
            new = []
            for node in nodes:
                operation(node)
                for child in node.children:
                    new.append(child)

            if len(new):
                _walk(new)

        if self.root:
            _walk([self.root])

    def print_level_order(self):
        count = 1
        newcount = 0
        stringthing = ''

        def _walk(nodes):
            nonlocal count, newcount, stringthing
            new = []
            if count > 0:
                for node in nodes:
                    stringthing += str(node.val)
                    count -= 1
                    for child in node.children:
                        newcount += 1
                        new.append(child)
            stringthing += '\n'
            count = newcount
            newcount = 0

            if len(new):
                _walk(new)

        if self.root:
            _walk([self.root])

        return stringthing
