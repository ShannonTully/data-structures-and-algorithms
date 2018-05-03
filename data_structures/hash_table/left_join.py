"""This function will left join two hash maps into one."""


def left_join(HM1, HM2):
    """Left join 2 hash maps."""
    final = dict()
    count = 0
    for bucket in HM1.buckets:
        node = bucket.head
        for each in range(len(bucket) - 1):
            final.update(node.val)
            node = node.next
            count += 1

    for bucket in HM2.buckets:
        node = bucket.head
        for each in range(len(bucket) - 1):
            for bucket1 in HM1.buckets:
                node1 = bucket1.head
                for each in range(len(bucket) - 1):
                    if node.val.items()[0][0] in node1.val:
                        # nope
