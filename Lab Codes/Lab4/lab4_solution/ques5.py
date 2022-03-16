def factorial(n):
    """Calculates n!
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combination(n, k):
    """Calculates n k combination by using its factorial definition
    """
    #n! / (n-k)! k!
    return factorial(n) / (factorial(n-k) * factorial(k))

result = combination(6, 4)
print(result)
