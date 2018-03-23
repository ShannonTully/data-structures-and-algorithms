def largest_product(a_list):
    if len(a_list) == 0:
        return False
    column = 0
    row = 0
    big = a_list[0][0] * a_list[0][1]
    while column < len(a_list) - 1:
        if a_list[column][row] * a_list[column][row + 1] > big:
            big = a_list[column][row] * a_list[column][row + 1]
        if a_list[column][row] * a_list[column + 1][row] > big:
            big = a_list[column][row] * a_list[column + 1][row]
        if a_list[column][row] * a_list[column + 1][row + 1] > big:
            big = a_list[column][row] * a_list[column + 1][row + 1]
        if a_list[column + 1][row] * a_list[column + 1][row + 1]:
            big = a_list[column + 1][row] * a_list[column + 1][row + 1]
        if a_list[column][row + 1] * a_list[column + 1][row + 1]:
            a_list[column][row + 1] * a_list[column + 1][row + 1]
        column += 1
    return big
