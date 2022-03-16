#Solution1

#get 2 numbers from user
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

#get the operation what the user wants
operation = str(input("Operation? (only use +,-,*,/):" ))

#define operations
addition = n1 + n2
substraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2

#conditions of operations
if operation == "+":
    print(addition)
if operation == "-":
    print(substraction)
if operation == "*":
    print(multiplication)
if operation == "/":
    print(division)    


#Solution2

for i in (10, 0, -1):
    print(i ** 2, end=' ')

