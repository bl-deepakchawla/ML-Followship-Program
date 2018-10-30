def matrix_transpose(l_mat1):
    return [[row[i] for row in l_mat1] for i in range(len(l_mat1[0]))]


g_mat1 = [[5, 8, 1],
          [6, 7, 3],
          [4, 5, 9]]

g_resultant_mat = matrix_transpose(g_mat1)
print("First Matrix is", g_mat1)
print("Inverse of first matrix is", g_resultant_mat)
