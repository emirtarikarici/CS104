#Get 3 number from user
n1 = int(input("Write the first number:"))
n2 = int(input("Write the second number:"))
n3 = int(input("Write the third number:"))

#Assign a variable for listing the numbers
numbers = [n1,n2,n3]

#Conditionals of sorting the numbers
if n1 > n2 > n3:
        print(str(n1) + " > " + str(n2) + " > " + str(n3))
elif n1 > n3 > n2:
        print(str(n1) + " > " + str(n3) + " > " + str(n2))
elif n1 > n2 == n3:
        print(str(n1) + " > " + str(n3) + " = " + str(n2))
elif n1 == n2 > n3:
        print(str(n1) + " = " + str(n2) + " > " + str(n3))
elif n1 == n3 > n2:
        print(str(n1) + " = " + str(n3) + " > " + str(n2))

elif n2 > n1 > n3:
        print(str(n2) + " > " + str(n1) + " > " + str(n3))
elif n2 > n3 > n1:
        print(str(n2) + " > " + str(n3) + " > " + str(n1))
elif n2 > n1 == n3:
        print(str(n2) + " > " + str(n3) + " = " + str(n1))
elif n2 == n3 > n1:
        print(str(n2) + " = " + str(n3) + " > " + str(n1))

elif n3 > n1 > n2:
        print(str(n3) + " > " + str(n1) + " > " + str(n2))
elif n3 > n2 > n1:
        print(str(n3) + " > " + str(n2) + " > " + str(n1))
elif n3 > n1 == n2:
        print(str(n3) + " > " + str(n1) + " = " + str(n2))

else:
        print(str(n1) + " = " + str(n3) + " = " + str(n2))

