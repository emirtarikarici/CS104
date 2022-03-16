def pow(base, exponent):
    if exponent == 0:
        return 1
    return base * pow(base, exponent - 1)


assert pow(3, 4) == 81
