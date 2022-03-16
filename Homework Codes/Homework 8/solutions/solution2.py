def get_recamans_sequence(n, sequence):
    if n == 0:
        sequence.append(n)
        return n
    else:
        value = get_recamans_sequence(n - 1, sequence)
        if (value - n) > 0 and (value - n) not in sequence:
            sequence.append(value - n)
            return value - n
        else:
            sequence.append(value + n)
            return value + n


def print_recamans_sequence(n):
    recamans_sequence = []
    get_recamans_sequence(n, recamans_sequence)
    print(recamans_sequence)


def test_get_recamans_sequence():
    recamans_sequence = []
    get_recamans_sequence(3, recamans_sequence)
    assert recamans_sequence == [0, 1, 3, 6]
    recamans_sequence = []
    get_recamans_sequence(5, recamans_sequence)
    assert recamans_sequence == [0, 1, 3, 6, 2, 7]
    recamans_sequence = []
    get_recamans_sequence(7, recamans_sequence)
    assert recamans_sequence == [0, 1, 3, 6, 2, 7, 13, 20]


if __name__ == "__main__":
    test_get_recamans_sequence()
    print_recamans_sequence(3)
    print_recamans_sequence(5)
    print_recamans_sequence(7)
