def forbidden_third(a, b):
    """
    >>> forbidden_third([0, 1, 1, 0], [1, 0, 1, 0])
    [[1, 0, None, None, 1], [0, 1, None, None, 1]]
    """
    n = len(a)
    x = [None] * n + [1]
    y = [None] * n + [1]
    for i in range(0, n):
        if a[i] == 0 and b[i] == 1:
            x[i] = 1
            y[i] = 0
        if a[i] == 1 and b[i] == 0:
            x[i] = 0
            y[i] = 1
    return [x, y]


def generate_matching(l):
    """
    >>> list(generate_matching([0, None, 1]))
    [[0, 0, 1], [0, 1, 1]]
    """
    if not None in l:
        yield l
    else:
        k = l.index(None)
        x0 = l[:k] + [0] + l[k+1:]
        for m in generate_matching(x0):
            yield m
        x1 = l[:k] + [1] + l[k+1:]
        for m in generate_matching(x1):
            yield m
        
