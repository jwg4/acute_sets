import logging
import random


def forbidden_third(a, b):
    """
    >>> forbidden_third([False, True, True, False], [True, False, True, False])
    [[True, False, None, None], [False, True, None, None]]
    """
    n = len(a)
    x = [None] * n
    y = [None] * n
    for i in range(0, n):
        if a[i] == False and b[i] == True:
            x[i] = True
            y[i] = False
        if a[i] == True and b[i] == False:
            x[i] = False
            y[i] = True
    return [tuple(x), tuple(y)]


def generate_matching(l):
    """
    >>> list(generate_matching([False, None, True]))
    [[False, False, True], [False, True, True]]
    """
    if not None in l:
        yield l
    else:
        k = l.index(None)
        x0 = tuple(l[:k] + (False,) + l[k+1:])
        for m in generate_matching(x0):
            yield m
        x1 = tuple(l[:k] + (True,) + l[k+1:])
        for m in generate_matching(x1):
            yield m


def gen_forbidden_set(vs):
    n = len(vs)
    for i in range(0, n):
        for j in range(i+1, n):
            for t in forbidden_third(vs[i], vs[j]):
                for l in generate_matching(t):
                    yield l


def forbidden_set(vs):
    return set(gen_forbidden_set(vs))


def find_small_overlap(current, target):
    n = len(target[0])
    forbidden = forbidden_set(current)
    logging.info("Dimension is %d." % (n, ))
    logging.info("Size of current set is %d." % (len(current), ))
    logging.info("Size of forbidden set is %d." % (len(forbidden), ))
    mx = 0
    candidate = []
    for i in range(0, 3**n):
        flips = [random.choice([True, False]) for t in range(0, n)]
        flipped_target = [ tuple((a != b) for (a, b) in zip(flips, t)) for t in target ] 
        non_overlap = [f for f in flipped_target if f not in forbidden]
        c = len(non_overlap)
        if c > mx:
            mx = c
            candidate = non_overlap
    if candidate:
        return [tuple((False,) + g) for g in current] + [tuple((True,) + g) for g in candidate]
    else:
        return [tuple((random.choice([True, False]),) + g) for g in current]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    initial = [
        (False, True, True),
        (True, False, True),
        (True, True, False),
    ]

    s = initial
    for i in range(0, 10):
        s = find_small_overlap(s, s)
        print(s)
