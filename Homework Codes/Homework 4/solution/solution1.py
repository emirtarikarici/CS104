def find_common(first_list, second_list):
    common_elements = []
    for element in first_list:
        if element in second_list and element not in common_elements:
            common_elements.append(element)
    return sum(common_elements)


print(find_common([4, 16, 17, 8, 12, 14, 19], [17, 7, 13, 11, 4, 19, 17, 6, 4, 1, 3, 6]))
