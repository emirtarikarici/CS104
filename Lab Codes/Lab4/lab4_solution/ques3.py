def factorial(n):
    """Calculates n!
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    	
#result = factorial(6)
#print(result)
