def function_for_case_a(value):
    return value not in (A | B) - (A & B)


def function_for_case_b(value):
    return value in (A | B) - (A & B)


def function_for_case_c(value):
    return value in A - B


def function_for_case_d(value):
    return value not in B


A = set([2, 3, 4, 5, 6, 7, 8])
B = set([7, 8, 9, 10])

# Check a
print("Check a")
# value = 2, expect False
print(" ", function_for_case_a(2))
# value = 9, expect False
print(" ", function_for_case_a(9))
# value = 7, expect True
print(" ", function_for_case_a(7))
# value = 11, expect True
print(" ", function_for_case_a(11))

print("Check b")
# Check b
# value = 2, expect True
print(" ", function_for_case_b(2))
# value = 9, expect True
print(" ", function_for_case_b(9))
# value = 7, expect False
print(" ", function_for_case_b(7))
# value = 11, expect False
print(" ", function_for_case_b(11))

print("Check c")
# Check c
# value = 2, expect True
print(" ", function_for_case_c(2))
# value = 9, expect False
print(" ", function_for_case_c(9))
# value = 7, expect False
print(" ", function_for_case_c(7))
# value = 11, expect False
print(" ", function_for_case_c(11))

print("Check d")
# Check d
# value = 2, expect True
print(" ", function_for_case_d(2))
# value = 9, expect False
print(" ", function_for_case_d(9))
# value = 7, expect False
print(" ", function_for_case_d(7))
# value = 11, expect True
print(" ", function_for_case_d(11))
