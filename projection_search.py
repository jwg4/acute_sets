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
            
                
if __name__ == '__main__':
    for i in range(0, 1000):
        s5 = generate_valid_set(5, 10)
        s4 = find_valid_projection(s5, 5, 4)
        if s4 is not None:
            break;
    print(s4)
