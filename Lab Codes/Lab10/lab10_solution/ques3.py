def steps(x) -> int:
    if x == 1:
        return 1
    elif x == 2:
        return x
    elif x == 3:
        return 4
    else:
        return steps(x-1) + steps(x-2) + steps(x-3)


result = steps(6)
print("Result is {0}".format(result))
