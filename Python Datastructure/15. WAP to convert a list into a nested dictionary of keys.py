def list_nested_dict(l_list):
    new_dict = temp = {}
    for value in l_list:
        temp[value] = {}
        temp = temp[value]
    return new_dict


g_list = [11, 12, 13, 14]
print("List values are, ", g_list)
results = list_nested_dict(g_list)
print("Nested dictionary are, ", results)
