from timeit import timeit, repeat


SETUP = """
from %s import check_whole_set
from example_set import get_example_set;
x = get_example_set(9, 5);
"""

def time_function(module_name):
    print(module_name)
    results = repeat('check_whole_set(x)', setup=SETUP % module_name, repeat=100, number=10000)
    print(sum(results))

time_function("checking") 
time_function("angle_routines.check") 
