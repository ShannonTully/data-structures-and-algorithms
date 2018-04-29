def merge_lists(l1, l2):
    runner1 = l1.head
    runner2 = l2.head
    while runner1 and runner2:
        temp = runner2._next
        runner1._next = runner2
        runner1 = runner2._next
        runner2 = temp
    return l1.head
