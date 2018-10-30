def multiply_matrix_with_scalar(l_mat1, l_scalar_number):
    l_resultant_mat = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
    for value1 in range(0, len(l_mat1)):
        for value2 in range(0, len(l_mat1[0])):
            l_resultant_mat[value1][value2] = l_mat1[value1][value2] * l_scalar_number
    return l_resultant_mat


g_mat1 = [[12, 7, 3],
          [4, 5, 6],
          [7, 8, 9]]
g_scalar_number = 9
g_resultant_mat = multiply_matrix_with_scalar(g_mat1, g_scalar_number)
print("First Matrix is", g_mat1)
print("Multiplication of a matrix with a scalar number is", g_resultant_mat)
