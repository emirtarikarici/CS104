def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(is_prime_number(7))  # True
print(is_prime_number(6))  # False
print(is_prime_number(5))  # True
print(is_prime_number(4))  # False
print(is_prime_number(3))  # True
print(is_prime_number(2))  # True
print(is_prime_number(1))  # False
print(is_prime_number(0))  # False
print(is_prime_number(-1))  # False
