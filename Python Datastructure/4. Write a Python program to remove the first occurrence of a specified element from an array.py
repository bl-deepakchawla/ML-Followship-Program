def remove_first_occurrence(l_arr_values, l_number):
    count = l_arr_values.count(l_number)
    if count <= 1:
        print('Number ', l_number, 'not occur more than 1 time')
    else:
        print("Array values ", l_arr_values, " before remove the first occurrence of number ", l_number)
        index_value = l_arr_values.index(l_number)
        l_arr_values.remove(l_arr_values[index_value])
        print("Array values ",  l_arr_values, " after remove the first occurrence of number ", l_number)


g_arr_values = [11, 12, 13, 13, 14, 15]
g_number = 13
remove_first_occurrence(g_arr_values, g_number)
