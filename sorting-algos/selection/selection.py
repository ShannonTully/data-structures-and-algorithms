"""The selection sorting algorithm."""


def selection(unsorted):
    """Take in an unsorted list and sort it using the selection sort method."""
    if len(unsorted) < 2:
        return unsorted

    for count in range(0, len(unsorted) - 1):
        minimum = count
        for each in range(count, len(unsorted)):
            if unsorted[each] < unsorted[minimum]:
                print('unsorted', unsorted)
                print('each', each, 'minimum', minimum)
                minimum = each

        unsorted[count], unsorted[minimum] = unsorted[minimum], unsorted[count]

    return unsorted
