def difference_list(l_list1, l_list2):
    l_list1 = set(l_list1)
    l_list2 = set(l_list2)
    differ_list = l_list1.difference(l_list2)
    return list(differ_list)


g_list1 = [11, 12, 13, 14, 15, 16]
g_list2 = [21, 22, 13, 24, 25, 26]
differ_list = difference_list(g_list1, g_list2)
print("List one values", g_list1)
print("List second values", g_list2)
print("Difference between two lists are ", differ_list)
