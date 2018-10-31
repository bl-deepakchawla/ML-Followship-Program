def multiply_two_matrix(l_mat1, l_mat2):
    l_resultant_mat = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for value1 in range(0, len(l_mat1)):
        for value2 in range(0, len(l_mat1[0])):
            for value3 in range(0, len(l_mat2)):
                l_resultant_mat[value1][value2] += l_mat1[value1][value3] * l_mat2[value3][value2]
    return l_resultant_mat


g_mat1 = [[12, 7, 3],
          [4, 5, 6],
          [7, 8, 9]]
g_mat2 = [[5, 8, 1],
          [6, 7, 3],
          [4, 5, 9]]

g_resultant_mat = multiply_two_matrix(g_mat1, g_mat2)
print("First Matrix is", g_mat1)
print("Second Matrix is", g_mat2)
print("Multiply of both matrix is", g_resultant_mat)
