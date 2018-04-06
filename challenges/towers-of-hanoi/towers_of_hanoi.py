# count = 0


def towers_of_hanoi(n):
    # global count
    left = ([], 'a')
    middle = ([], 'b')
    right = ([], 'c')
    for each in reversed(range(n)):
        left[0].append(each)
    return recursion(n, left, middle, right)
    # return count


def recursion(n, a, b, c):
    # global count
    count = 0
    end = ''
    if n > 0:
        bob = recursion(n - 1, a, c, b)
        if a[0]:
            ring = a[0].pop()
            end = ('Disk {} moved from {} to {}'.format(ring + 1, a[1], c[1]))
            count += 1
            print(end)
            c[0].append(ring)
        mary = recursion(n - 1, b, a, c)
        count = count + bob + mary
    return count
