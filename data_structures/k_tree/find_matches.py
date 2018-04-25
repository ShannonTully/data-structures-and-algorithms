"""Find matching values in k-nary tree."""


def find_matches(tree, val):
    """Find the matches."""
    new = []

    def find(node):
        nonlocal new, val
        if val == node.val:
            new.append(node)

    tree.pre_order(find)

    if new:
        return new
    else:
        return False
