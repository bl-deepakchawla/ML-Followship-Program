def unique_values_dic(l_dict_values):
    new_dict = set([val for dic in l_dict_values for val in dic.values()])
    return new_dict


g_dict_values = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Dictionary contained values are,", g_dict_values)
g_unique_values = unique_values_dic(g_dict_values)
print("Unique values in dictionary are, ", g_unique_values)
