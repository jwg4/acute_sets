import time

from points import generate_valid_set


def time_valid_set(limit):
    t = time.clock()
    total_time = 0
    total = 0
    while total_time < 3600:
        results = [ generate_valid_set(5, 9, limit) for x in range(0, 1000) ]
        total = len([s for s in results if s is not None])
        total_time = time.clock() - t
    return total, total_time
        
        
if __name__ == '__main__':
    for i in range(1, 10):
        c, t = time_valid_set(i * 200)
        if c:
            print("%d results in %f seconds: %f seconds per result." % (c, t, t/c))
        else:
            print("No results in %f seconds." % (t, ))
    
