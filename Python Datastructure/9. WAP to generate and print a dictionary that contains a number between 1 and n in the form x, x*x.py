def dict_multiply_form(l_n):
    l_dict = {}

    for l_n in range(l_n):
        l_dict.update({l_n: (l_n * l_n)})

    return l_dict


g_n = 5
g_resultant_dict = dict_multiply_form(g_n)
print("Generated dictionary is, ", g_resultant_dict)
