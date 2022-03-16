def isPrime(n, i = 2):
    """ Returns true if n is prime, else return false.
        i is current divisor to check.
    """
    # Base cases
    if n <= 2:
        return_value = True if n == 2 else False
        return return_value
    if n % i == 0:
        return False
    if i * i > n:
        return True

    # Check for next divisor
    return isPrime(n, i + 1)

n = 11
if isPrime(n):
    print("Yes")
else:
	print("No")
