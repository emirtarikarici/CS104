def multiply_matrix_and_vector(matrix, vector):
    return [sum([matrix[i][j] * vector[j] for j in range(len(vector))]) for i in range(len(matrix))]


A = [[1, 2], [-1, 1]]
x = [5, 4]

# Expect b = [13, -1]
b = multiply_matrix_and_vector(A, x)
print(b)
