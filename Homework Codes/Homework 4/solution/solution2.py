def verify_isbn_number(isbn_number):
    total = 0
    for i in range(len(isbn_number)):
        total += int(isbn_number[i]) * (10 - i)
    return total % 11 == 0


print(verify_isbn_number("0536000069"))
print(verify_isbn_number("0321334877"))
