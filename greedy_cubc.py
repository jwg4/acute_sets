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
    return [x, y]


def generate_matching(l):
    """
    >>> list(generate_matching([False, None, True]))
    [[False, False, True], [False, True, True]]
    """
    if not None in l:
        yield l
    else:
        k = l.index(None)
        x0 = l[:k] + [False] + l[k+1:]
        for m in generate_matching(x0):
            yield m
        x1 = l[:k] + [True] + l[k+1:]
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
    return list(gen_forbidden_set(vs))


def find_small_overlap(current, target):
    n = len(target[0])
    forbidden = forbidden_set(current)
    expanded = [v + [1] for v in target]
    mx = 0
    candidate = None
    for i in range(0, 10000):
        flips = [random.choice([True, False]) for t in range(0, n)]
        flipped_target = [ [(a != b) for (a, b) in zip(flips, t)] for t in target ] 
        non_overlap = [f for f in flipped_target if f not in forbidden]
        c = len(non_overlap)
        if c > mx:
            mx = c
            candidate = non_overlap
    if candidate:
        return [[0] + g for g in current] + [[1] + g for f in candidate]


if __name__ == '__main__':
    initial = [
        [False, False, False],
        [False, True, True],
        [True, False, True],
        [True, True, False],
    ]

    print(find_small_overlap(initial, initial))
