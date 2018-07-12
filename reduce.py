from points import check_whole_set


def parse_data_file(filename):
    with open(filename, "r") as f:
        l = []
        for line in f.readlines():
            if line.startswith("---"):
                yield l
                l = []
            else:
                t = tuple(int(x) for x in line.split("\t"))
                l.append(t)
        yield l
            

def reduce_by_2(points):
    return [
        tuple(x//2 for x in t)
        for t in points
    ]


if __name__ == '__main__':
    filename = "data/9.txt"
    for pointset in parse_data_file(filename):
        reduced = None
        while check_whole_set(pointset):
            reduced = pointset
            pointset = reduce_by_2(pointset)
        print(reduced)
