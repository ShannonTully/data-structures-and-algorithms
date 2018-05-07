"""The merge sorting algorithm."""


def mergesort(unsorted):
    """Take in an unsorted list and sort it recursivly using the merge sort method."""
    if len(unsorted) < 2:
        return unsorted

    left = []
    right = []
    count = 0

    for item in unsorted:
        if count < len(unsorted) / 2:
            left.append(item)
            count += 1
        else:
            right.append(item)
            count += 1

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    """Merge helper for the merge sort."""
    final = []
    leftcount = 0
    rightcount = 0

    while leftcount < len(left) and rightcount < len(right):
        if left[leftcount] < right[rightcount]:
            final.append(left[leftcount])
            leftcount += 1
        else:
            final.append(right[rightcount])
            rightcount += 1

    while leftcount < len(left):
        final.append(left[leftcount])
        leftcount += 1

    while rightcount < len(right):
        final.append(right[rightcount])
        rightcount += 1

    return final
