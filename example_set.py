import random


def get_example_set(size, dimension, maxint=65535):
    return [
        tuple(random.randint(0, maxint) for i in range(0, dimension))
        for j in range(0, size)
    ]
