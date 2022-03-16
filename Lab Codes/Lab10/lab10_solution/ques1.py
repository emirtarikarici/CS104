def gcd(x, y) -> int:
    if y == 0:
        return x
    else:
        print(str(y) + " " + str(x % y))
        return gcd(y, x % y)


result = gcd(219, 93)
print("Result is {}".format(result))
