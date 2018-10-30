def multiply_matrix_with_vector(l_mat1, l_mat2):

    l_resultant_mat = [[0, 0, 0]]

    for value1 in range(0, len(l_mat1)):
        for value2 in range(0, len(l_mat1[0])):
            l_resultant_mat[0][value1] += l_mat1[value1][value2] * l_mat2[0][value2]

    return l_resultant_mat


g_mat1 = [[5, 1, 3],
         [1, 1, 1],
         [1, 2, 1]]

g_mat2 = [[1, 2, 3]]

g_resultant_mat = add_two_matrix(g_mat1, g_mat2)

print("First Matrix is", g_mat1)
print("Second Matrix is", g_mat2)
print("Sum of both matrix is", g_resultant_mat)
