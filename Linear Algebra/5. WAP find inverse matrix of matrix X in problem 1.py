def matrix_inverse(l_mat1):
    return [[row[i] for row in l_mat1] for i in range(len(l_mat1[0]))]


g_mat1 = [[12, 7, 3],
          [4, 5, 6],
          [7, 8, 9]]
g_resultant_mat = matrix_inverse(g_mat1)
print("First Matrix is", g_mat1)
print("Transpose of first matrix is", g_resultant_mat)
