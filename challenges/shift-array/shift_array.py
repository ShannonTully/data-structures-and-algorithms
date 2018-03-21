def insertShiftArray(array, val):
    new_array = array + ['']
    count = 0
    for i in array:
        if count == len(array) / 2:
            new_array[count] = val
            count += 1
        new_array[count] = i
        count += 1
    return new_array
