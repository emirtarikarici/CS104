import binary_search as bs
import linear_search as ls
import time
import random

if __name__ == '__main__':
    # linear search
    sizes = [10, 100, 1000, 10000, 1000000, 10000000]
    for size in sizes:
        f = open("linear_search_times.csv", "a")
        try:
            sequence = range(1, size)
            values = [random.randint(1, size - 1) for i in range(10)]
            for value in values:
                start_time = time.time()
                ls.linear_search(sequence, value)
                stop_time = time.time()
                record = str(size) + "," + str(value) + "," + str(stop_time - start_time) + "\n"
                f.write(record)
        except ValueError:
            print("Value is not in data")
        f.close()

    # binary search
    sizes = [10, 100, 1000, 10000, 1000000, 10000000]
    for size in sizes:
        f = open("binary_search_times.csv", "a")
        try:
            sequence = range(1, size)
            values = [random.randint(1, size - 1) for i in range(10)]
            for value in values:
                start_time = time.time()
                bs.binary_search(sequence, value)
                stop_time = time.time()
                record = str(size) + "," + str(value) + "," + str(stop_time - start_time) + "\n"
                f.write(record)
        except ValueError:
            print("Value is not in data")
        f.close()
