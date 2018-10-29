def common_in_two_list(l_list1, l_list2):
    count = 0
    for value1 in l_list1:
        if value1 in l_list2:
            count += 1
    if count >= 1:
        return True
    else:
        return False


g_list1 = [11, 12, 13, 14, 15, 16]
g_list2 = [21, 22, 13, 24, 25, 26]
result = common_in_two_list(g_list1, g_list2)
print(result)
