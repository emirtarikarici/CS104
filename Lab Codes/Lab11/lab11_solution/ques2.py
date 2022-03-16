import time

def factorial_recursive(n):  
    return 1 if (n==1 or n==0) else n * factorial_recursive(n - 1);  

def factorial_iterative(n):
    factorial = 1    
    if n < 0:    
        print(" Factorial does not exist for negative numbers")    
    elif n == 0:    
        return factorial   
    else:    
        for i in range(1,n + 1):    
            factorial = factorial*i    

    return factorial

number = 10
t1 = time.time()
print("Recursive factorial is is", factorial_recursive(number))
t2 = time.time()
print("Recursive method runs in {0} seconds".format(t2-t1))

t1 = time.time()
print("Iterative factorial is is", factorial_iterative(number))  
t2 = time.time()
print("Iterative method runs in {0} seconds".format(t2-t1))
