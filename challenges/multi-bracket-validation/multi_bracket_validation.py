def multi_bracket_validation(bracket_string):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for item in bracket_string:
        if item is '(':
            counter1 += 1
        elif item is ')':
            counter1 -= 1
        elif item is '{':
            counter2 += 1
        elif item is '}':
            counter2 -= 1
        elif item is '[':
            counter3 += 1
        elif item is ']':
            counter3 -= 1
    if counter1 == 0 and counter2 == 0 and counter3 == 0:
        return True
    else:
        return False
