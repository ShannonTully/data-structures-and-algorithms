def binary_search(sorted_list, key):
    if type(key) is not int:
        raise TypeError('Argument invalid. Must be int.')
    left = 0
    right = len(sorted_list) - 1
    while left != right:
        # import pdb; pdb.set_trace()
        if (left + right) % 2:
            if sorted_list[int((left + right) / 2)] == key:
                return int((left + right) / 2)
            if sorted_list[int((left + right) / 2)] > key:
                right = int((left + right) / 2)
            else:
                left = int((left + right) / 2)
        elif sorted_list[int((left + right + 1) / 2)] == key:
            return int((left + right + 1) / 2)
        if sorted_list[int((left + right + 1) / 2)] == key:
            return int((left + right + 1) / 2)
        if sorted_list[int((left + right + 1) / 2)] > key:
            right = int((left + right + 1) / 2)
        else:
            left = int((left + right + 1) / 2)
    return 0 - 1


if __name__ == '__main__':
    binary_search([4, 8, 15, 16, 23, 42], 42)