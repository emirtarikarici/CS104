def population(year):
    if year == 0:
        return 1000000
    else:
        return population(year-1)*1.01 + 1000


result = population(10)
print("Result is {0}".format(result))
