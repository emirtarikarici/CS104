def is_matrix_symmetric(matrix):
    diagonal = []
    is_symmetric = True
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
        if is_symmetric:
            for j in range(i):
                if matrix[i][j] != matrix[j][i]:
                    is_symmetric = False
                    break
    print(is_symmetric)

    return diagonal


# expect True and [11, 10, 3, 44]
matrix_a = [[11, 2, 13, 1], [2, 10, 5, 24], [13, 5, 3, 4], [1, 24, 4, 44]]
print(is_matrix_symmetric(matrix_a))
# expect False and [11, 10, 3, 47]
matrix_b = [[11, 2, 130, 1], [4, 10, 5, 4], [3, 5, 3, 41], [51, 24, 4, 47]]
print(is_matrix_symmetric(matrix_b))
# expect True and [4.420, 3.832, 3.207]
matrix_c = [[4.420, 1.35, 3.509], [1.35, 3.832, 0.], [3.509, 0., 3.207]]
print(is_matrix_symmetric(matrix_c))
# expect False and [11.23, 11.23]
matrix_d = [[11.23, 1.9], [100.6, 11.23]]
print(is_matrix_symmetric(matrix_d))
