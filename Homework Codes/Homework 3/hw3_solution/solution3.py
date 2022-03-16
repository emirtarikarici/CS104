def get_row(row_height):
    row = ""
    for i in range(1, row_height + 1):
        row += str(i) + " "
    for i in range(row_height - 1, 0, -1):
        row += str(i) + " "
    return row


def print_triangle(height):
    for row in range(1, height + 1):
        print(" " * (height - row) * 2 + get_row(row))
    return height ** 2


print("Sum of all integers on the last line is", print_triangle(4))
print()
print("Sum of all integers on the last line is", print_triangle(2))
print()
print("Sum of all integers on the last line is", print_triangle(7))
