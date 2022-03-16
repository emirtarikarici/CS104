import math

def Convert_10_to_2_R(n, k):
    """ Recursive function. Converting a number from the 10th number system to binary.
        The function returns the result as a number: 13 => 1101.
        Parameters:
            - n - the number in the decimal system;
            - k - the current order (number of digits) of the number in the binary system.
    """
    if n>0:
        t = n%2
        return Convert_10_to_2_R(n//2, k+1) + int(t*math.pow(10,k))
    else:
        return 0

def Convert_10_to_2(n):
    """ Non recursive convertion function
    """
    summ = 0 # the sum of numbers: 5 => 100 + 0 + 1 => 101
    k = 0 # the order of number in the binary system

    while n>0:
        t = n%2
        summ = summ + int(t*math.pow(10,k))
        k = k+1
        n = n//2

    return summ

# Demonstration of using functions
res1 = Convert_10_to_2_R(126, 0)
res2 = Convert_10_to_2(126) 
print("res1 = " , res1)
print("res2 = " , res2)
