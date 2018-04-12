def find_maximum_value_binary_tree(tree):
    high = None

    def find_max(node):
        nonlocal high

        high = node.val if high is None or node.val > high else high

    tree.pre_order(find_max)
    
    return high


