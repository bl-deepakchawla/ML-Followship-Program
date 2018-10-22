def sort_dictionay_values(l_dict_values):
    l_asc_sorted_values = {}
    l_desc_sorted_values = {}

    temp_l_asc_sorted_values = sorted(l_dict_values, key=l_dict_values.get)
    temp_l_desc_sorted_values = sorted(l_dict_values, key=l_dict_values.get, reverse=True)

    for r in temp_l_asc_sorted_values:
        l_asc_sorted_values.update({r: l_dict_values[r]})

    for r in temp_l_desc_sorted_values:
        l_desc_sorted_values.update({r: l_dict_values[r]})

    return [l_asc_sorted_values, l_desc_sorted_values]


g_dict_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

print("Orignal dictionary values before sorting are, ", g_dict_values)

sorted_g_dic_values = sort_dictionay_values(g_dict_values)

print("Dictionary values after sorting are in ascending order are, ", sorted_g_dic_values[0])

print("Dictionary values after sorting are in descending order are, ", sorted_g_dic_values[1])