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
