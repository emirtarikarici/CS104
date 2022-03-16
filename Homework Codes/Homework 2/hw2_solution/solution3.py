counter = 0
number = 2
is_prime = True
while counter < 20:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)
        counter += 1
    is_prime = True
    number += 1
