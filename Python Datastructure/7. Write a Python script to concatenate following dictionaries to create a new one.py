def concatenate_multiple_dicts(l_dic1, l_dic2, l_dic3):

    new_dic = {}
    new_dic.update(l_dic1)
    new_dic.update(l_dic2)
    new_dic.update(l_dic3)

    return new_dic


g_dic1 = {1: 10, 2: 20}
g_dic2 = {3: 30, 4: 40}
g_dic3 = {5: 50, 6: 60}

resultant_dict = concatenate_multiple_dicts(g_dic1, g_dic2, g_dic3)

print("Dict 1 values, ", g_dic1)
print("Dict 2 values, ", g_dic2)
print("Dict 3 values, ", g_dic3)
print("Dictionary after concatenate the all three dictionary is, ", resultant_dict)