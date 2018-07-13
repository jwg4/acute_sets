def check_angle(short a, short b, short c):
    ba = tuple(x[0] - x[1] for x in zip(a, b))
    bc = tuple(x[0] - x[1] for x in zip(c, b))
    inner = tuple(x[0] * x[1] for x in zip(ba, bc))
    s = sum(inner)
    return s > 0
