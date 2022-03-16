total = 0
user_input = 0
while user_input >= 0:
    user_input = float(input("Please enter a number: "))
    if user_input < 0:
        break
    total += user_input

print("Sum of all numbers is", total)
