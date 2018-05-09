"""The quick sort algorithm."""


def quicksort(unsorted, low=0, high=False):
    """Quick sort a list."""
    if len(unsorted) < 2:
        return unsorted

    if high is False:
        high = len(unsorted) - 1

    if low < high:
        swapper = swap(unsorted, low, high)
        quicksort(unsorted, low, swapper - 1)
        quicksort(unsorted, swapper + 1, high)

    return unsorted


def swap(sort, low, high):
    """Swap the items."""
    count = low

    for index in range(low + 1, high + 1):
        if sort[index] <= sort[low]:
            count += 1
            sort[count], sort[index] = sort[index], sort[count]

    sort[count], sort[low] = sort[low], sort[count]

    return count
