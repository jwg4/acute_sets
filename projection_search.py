import logging

from points import check_whole_set, generate_random_point, generate_valid_set


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

    for i in range(0, 100000):
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
