def luhn_sum_double(n):
    # Return the Luhn sum of n, doubling the last digit.
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


def luhn_sum(n):
    # Return the digit sum of n computed by the Luhn algorithm
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def split(n):
    return n // 10, n % 10


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


assert luhn_sum(9) == 9
assert luhn_sum(12) == 4
assert split(1234) == (123, 4)
assert split(5) == (0, 5)
assert sum_digits(8) == 8
assert sum_digits(0) == 0
assert sum_digits(18) == 9
assert luhn_sum(138743) == 30
assert luhn_sum_double(3) == 6
assert luhn_sum_double(34) == 11
