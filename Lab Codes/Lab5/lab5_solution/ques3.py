def findDivisors (n1, n2):
    """Assumes that n1 and n2 are positive ints
       Returns a tuple containing all common divisors of n1 & n2"""
    divisors = [] #the empty tuple
    for i in range(1, min (n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors.append(i)

    return divisors

divisors = findDivisors(20, 100)
print(divisors)
total = sum([d for d in divisors])
print(total)
