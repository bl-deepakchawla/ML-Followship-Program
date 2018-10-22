def create_dict_from_string(l_string):
    new_dict = {}
    str_to_dict = list(l_string)
    temp_dict = set([val for dic in str_to_dict for val in dic])
    for value in temp_dict:
        new_dict.update({value:str_to_dict.count(value)})
    return new_dict


g_string = 'w3resource'
g_resultant_dict = create_dict_from_string(g_string)
print("String is ", g_string)
print('Resultant dictionary from the string is,' , g_resultant_dict)
