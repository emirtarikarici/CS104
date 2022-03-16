# Letter O
for i in range(9):
    for j in range(7):
        if j == 0 or j == 6:
            if i == 0 or i == 8:
                print(" ", end="")
            else:
                print("O", end="")
        else:
            if i == 0 or i == 8:
                print("O", end="")
            else:
                print(" ", end="")
    print()
print()

# Letter Z
for i in range(9):
    for j in range(7):
        if i == 0 or i == 8:
            print("Z", end="")
        elif j == 7 - i:
            print("Z", end="")
        else:
            print(" ", end="")
    print()
print()

# Letter U
for i in range(9):
    for j in range(7):
        if j == 0 or j == 6:
            if i == 8:
                print(" ", end="")
            else:
                print("U", end="")
        elif i == 8:
            print("U", end="")
        else:
            print(" ", end="")
    print()
print()
