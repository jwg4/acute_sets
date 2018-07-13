from cython import sizeof
from cpython cimport array
from libc.stdlib cimport malloc
import array

cdef int check_angle(int[] a, int[] b, int[] c, int d):
    cdef int i
    cdef int s
    for i in range(d):
        s = s + (a[i] - b[i]) * (c[i] - b[i])
    return s > 0


cdef int check_triplet(int[] a, int[] b, int[] c, int d):
    return check_angle(a, b, c, d) and check_angle(b, c, a, d) and check_angle(c, a, b, d)


cdef int** array_points(points, int n, int d):
    cdef int** a_points;
    cdef int* p;
    a_points = <int **>malloc(n*sizeof(p))

    for i in range(n):
        p = <int *>malloc(d*sizeof(int))
        for j in range(d):
            p[j] = points[n][d]
        a_points[i] = p

    return a_points


def check_whole_set(points):
    cdef int n = len(points)
    cdef int d = len(points[0])
    a_points = array_points(points, n, d)
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not check_triplet(a_points[i], a_points[j], a_points[k], d):
                    return False
    return True
