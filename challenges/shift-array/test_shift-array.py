import shift_array


def test_value_gets_placed_in_middle_of_array():
    assert shift_array.insertShiftArray([1, 2, 3, 4], 5) == [1, 2, 5, 3, 4]