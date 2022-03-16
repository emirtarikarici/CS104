# In number theory, a “perfect number” is a positive integer 
# that is equal to the sum of its positive divisors (excluding the number itself). 
# If sum of its positive divisors is greater than the number itself, 
# such number is called “abundant number”. 
# Lastly, number is called a “deficient number” when the sum of its positive divisors is less than the number itself
# Write a program that prints out all the perfect numbers between 0 and inputted range. 
# Additionally, it prints out the number of abundant and deficient numbers.

perfect = []
abundant = []
deficient = []

nmbr = int(input("Write a number: "))

for i in range(1,nmbr):
    if nmbr % i == 0:
        perfect.append(nmbr)    
        print(perfect)
    # elif nmbr % i > 0