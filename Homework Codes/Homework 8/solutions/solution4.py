import math
import time


def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def non_recursive_fibonacci(n):
    return round((math.pow((1 + math.sqrt(5)) / 2, n + 1) - math.pow((1 - math.sqrt(5)) / 2, n + 1)) / math.sqrt(5))


def golden_ratio_by_recursive_fibonacci(n):
    return recursive_fibonacci(n + 1) / recursive_fibonacci(n)


def golden_ratio_by_non_recursive_fibonacci(n):
    return non_recursive_fibonacci(n + 1) / non_recursive_fibonacci(n)


assert recursive_fibonacci(0) == 1
assert recursive_fibonacci(1) == 1
assert recursive_fibonacci(2) == 2
assert recursive_fibonacci(3) == 3
assert recursive_fibonacci(4) == 5

assert non_recursive_fibonacci(0) == 1
assert non_recursive_fibonacci(1) == 1
assert non_recursive_fibonacci(2) == 2
assert non_recursive_fibonacci(3) == 3
assert non_recursive_fibonacci(4) == 5

assert golden_ratio_by_recursive_fibonacci(0) == 1
assert golden_ratio_by_recursive_fibonacci(1) == 2
assert golden_ratio_by_recursive_fibonacci(2) == 1.5
assert golden_ratio_by_recursive_fibonacci(4) == 1.6

assert golden_ratio_by_non_recursive_fibonacci(0) == 1
assert golden_ratio_by_non_recursive_fibonacci(1) == 2
assert golden_ratio_by_non_recursive_fibonacci(2) == 1.5
assert golden_ratio_by_non_recursive_fibonacci(4) == 1.6

if __name__ == '__main__':
    sizes = [10, 20, 30, 40]
    for n in sizes:
        f = open("recursive_golden_ratio_computation_times.csv", "a")
        start_time = time.time()
        golden_ratio_calculated = golden_ratio_by_recursive_fibonacci(n)
        stop_time = time.time()
        record = str(n) + "," + str(golden_ratio_calculated) + "," + str(stop_time - start_time) + "\n"
        f.write(record)
        f.close()
        f = open("non_recursive_golden_ratio_computation_times.csv", "a")
        start_time = time.time()
        golden_ratio_calculated = golden_ratio_by_non_recursive_fibonacci(n)
        stop_time = time.time()
        record = str(n) + "," + str(golden_ratio_calculated) + "," + str(stop_time - start_time) + "\n"
        f.write(record)
        f.close()
