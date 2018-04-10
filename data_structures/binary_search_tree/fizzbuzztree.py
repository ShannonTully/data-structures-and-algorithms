def FizzBuzzTree(bst):
    if bst.root:
        return bst.pre_order(fizz_buzz)
    else:
        return False


def fizz_buzz(node):
    if node.val % 3 == 0:
        if node.val % 5 == 0:
            node.val = "fizzbuzz"
        else:
            node.val = "fizz"
    elif node.val % 5 == 0:
        node.val = "buzz"
