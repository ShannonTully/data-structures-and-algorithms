"""Take two Binary Trees and return a set of the intersection."""


def tree_intersection(BST1, BST2):
    """Find intersection."""
    set1 = set()
    set2 = set()
    list1 = []
    list2 = []

    BST1.in_order(list1.append)
    BST2.in_order(list2.append)

    for node in list1:
        set1.add(node.val)

    for node in list2:
        set2.add(node.val)

    if set1 & set2:
        return set1 & set2
    else:
        return
