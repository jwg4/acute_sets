from timeit import timeit


print("checking.check_angle")
timeit('check_angle((1,2,3), (2,3,4), (3,4,5))', setup='from checking import check_angle')
print("angle_routines.check.check_angle")
timeit('check_angle((1,2,3), (2,3,4), (3,4,5))', setup='from angle_routines.check import check_angle')
