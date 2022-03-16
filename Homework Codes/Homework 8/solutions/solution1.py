def get_first_digit(n):
    if n < 10:
        return n
    return get_first_digit(n // 10)


def get_digit_count(n):
    if n < 10:
        return 1
    return 1 + get_digit_count(n // 10)


def is_palindrome(n):
    if n < 10:
        return True
    return get_first_digit(n) == n % 10 and is_palindrome((
            n - n % 10 - get_first_digit(n) * 10 ** (get_digit_count(n) - 1) // 10))

    assert is_palindrome(2)
    assert is_palindrome(212)
    assert is_palindrome(99)
    assert is_palindrome(2123443212)
    assert not is_palindrome(213)
    assert not is_palindrome(43)
