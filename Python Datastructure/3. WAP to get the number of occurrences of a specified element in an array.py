def occurrences_number_in_array(l_arr_values, l_number):
    count = l_arr_values.count(l_number)
    print("Occurrences of number ", l_number, " in array " , l_arr_values, " is ", count)


g_arr_values = [11, 12, 13, 14, 14, 15]
g_number = 14
occurrences_number_in_array(g_arr_values, g_number)