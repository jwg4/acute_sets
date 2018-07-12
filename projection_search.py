import logging

from random import randint


def check_angle(a, b, c):
    d = len(a)
    s = 0
    for i in range(0, d):
        s = s + (a[i] - b[i]) * (c[i] - b[i])
    return s > 0


def check_triplet(a, b, c):
    return check_angle(a, b, c) and check_angle(b, c, a) and check_angle(c, a, b)


def check_new_point(point, points):
    n = len(points)
    for i in range(0, n):
        for j in range(i + 1, n):
            if not check_triplet(point, points[i], points[j]):
                return False
    return True


def check_whole_set(points):
    n = len(points)
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not check_triplet(points[i], points[j], points[k]):
                    return False
    return True


def generate_random_point(dimension, limit=65535):
    return tuple(randint(0, limit) for i in range(0, dimension))


def generate_valid_set(dimension, size):
    for bt_count in range(0, 1000):
        l = [None] * size
        for i in range(0, size):
            for point_count in range(0, 1000):
                p = generate_random_point(dimension)
                if check_new_point(p, l[:i]):
                    l[i] = p
                    break
            else:
                break
        else:
            return l
            


def project(p, v):
    V = sqrt(sum(x * x for x in v))
    n = len(p)
    pp = [None] * n
    for i in range(0, n):
        pp[i] = p[i] * (1.0 - (v[i] / V))
    return pp


def find_valid_projection(points, start_d, end_d):
    if start_d - end_d != 1:
        raise NotImplementedError()
           
    for p_count in range(0, 10000):
        v = generate_random_point(start_d) 
        projected = [ project(p, v) for p in points ]
        if check_whole_set(projected):
            return projected 
    return None

                
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    for i in range(0, 1000):
        s5 = generate_valid_set(5, 10)
        if s5 is None:
            logging.info("Couldnt find a valid set.")
            continue
        s4 = find_valid_projection(s5, 5, 4)
        if s4 is not None:
            break
        else:
            logging.info("Couldnt find a valid projection.")
    print(s4)
