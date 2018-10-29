def common_items_list(l_list1, l_list2):
    l_list1 = set(l_list1)
    l_list2 = set(l_list2)
    common_list = l_list1.intersection(l_list2)
    return list(common_list)


g_list1 = [11, 12, 13, 14, 15, 16]
g_list2 = [21, 12, 13, 24, 25, 26]
append_list = common_items_list(g_list1[:], g_list2)
print("List one values", g_list1)
print("List second values", g_list2)
print("Common lists items are ", append_list)
