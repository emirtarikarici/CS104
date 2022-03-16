def sum_recursively(input_list):
    if not input_list:
        return 0
    return input_list[0] + sum_recursively(input_list[1:])


assert sum_recursively([19, 5, 6]) == 30
