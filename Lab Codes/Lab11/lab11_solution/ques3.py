import time

def fibonacci_recursive(n):
    """ Recursive Function for nth Fibonacci number
    """
    # Check if input is 0 then it will print incorrect input
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_closed(N):
    g = (1 + 5**.5) / 2  # Golden ratio.
    return int((g**N - (1-g)**N) / 5**.5)

N = 20
t1 = time.time()
print(fibonacci_recursive(N))
t2 = time.time()
print("Recursive Fibonacci method runs in {0} seconds".format(t2-t1))

t1 = time.time()
print(fibonacci_closed(N))
t2 = time.time()
print("Closed form Fibonacci method runs in {0} seconds".format(t2-t1))
