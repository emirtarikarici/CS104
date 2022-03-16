def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')


if __name__ == '__main__':
    try:
        n = 10000000
        value_to_look_for = 350000
        data = range(1, n)
        print(linear_search(data, value_to_look_for))
    except ValueError:
        print("Value is not in data")
