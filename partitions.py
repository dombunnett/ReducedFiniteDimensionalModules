# PARTITION FUNTIONS
# Both ripped from overflow questions, slightly modified to
# return tuples with numbers in reverse order.
# The function quick_partition is much much better.

def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y, reverse=True)))
    return answer



def quick_partition(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield tuple(sorted(a[:k + 2], reverse=True))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield tuple(sorted(a[:k + 1], reverse = True))
