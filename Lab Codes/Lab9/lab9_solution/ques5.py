def primes_list_buggy(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    if i == 2:
        primes.append(2)
    # go through each elem of primes list
    for i in range(len(primes)):
        # go through each of 2...n
        for j in range(len(n)):
           # check if not divisible by elem of list
            if i%j != 0:
                primes.append(i)

def primes_list_correct(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    primes = [2]
    # go through each of 3...n
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

print(primes_list_correct(2))               
print(primes_list_correct(15))
#print(primes_list_buggy(2))               
#print(primes_list_buggy(15)) 
