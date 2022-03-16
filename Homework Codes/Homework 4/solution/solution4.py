possible_moves = [[2, 1], [1, 2], [2, -1], [-1, 2], [-2, 1], [1, -2], [-2, -1], [-1, -2]]


def return_possible_locations_for_knight_move(i, j):
    possible_locations = []
    for possible_move in possible_moves:
        if i + possible_move[0] < 0 or i + possible_move[0] > 7:
            continue
        if j + possible_move[1] < 0 or j + possible_move[1] > 7:
            continue
        possible_locations.append([i + possible_move[0], j + possible_move[1]])
    return possible_locations


print(return_possible_locations_for_knight_move(3, 4))
print(return_possible_locations_for_knight_move(0, 0))
print(return_possible_locations_for_knight_move(7, 0))
print(return_possible_locations_for_knight_move(7, 7))
print(return_possible_locations_for_knight_move(0, 7))
print(return_possible_locations_for_knight_move(0, 4))
print(return_possible_locations_for_knight_move(1, 3))
print(return_possible_locations_for_knight_move(3, 7))
print(return_possible_locations_for_knight_move(6, 1))
