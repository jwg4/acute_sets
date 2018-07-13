from random import randint

from checking import check_new_point


def generate_random_point(dimension, limit=65535):
    return tuple(randint(0, limit) for i in range(0, dimension))


def generate_valid_set(dimension, size, depth=1000):
    l = [None] * size
    for i in range(0, size):
        for point_count in range(0, depth):
            p = generate_random_point(dimension)
            if check_new_point(p, l[:i]):
                l[i] = p
                break
        else:
            break
    else:
        return l
