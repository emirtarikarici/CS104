print("Welcome to calculator!")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Choose one of the following operations:")
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
option = int(input(""))

if (option == 1):
    result = a + b
elif (option == 2):
    result = a - b
elif (option == 3):
    result = a * b
elif (option == 4):
    result = a / b
if option > 0 and option < 5:
    print("result: %f" % (result))
else:
    print("Invalid option")
print("Thank you for using our calculator.")
