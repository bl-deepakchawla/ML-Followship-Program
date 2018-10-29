def append_list_each_other(l_list1, l_list2):
    for value in l_list2:
        l_list1.append(value)
    return l_list1


g_list1 = [11, 12, 13, 14, 15, 16]
g_list2 = [21, 22, 13, 24, 25, 26]
append_list = append_list_each_other(g_list1[:], g_list2)
print("List one values", g_list1)
print("List second values", g_list2)
print("Appended lists are ", append_list)
