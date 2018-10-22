def count_no_of_items_dict(l_dic):
    total_count = sum(map(len, l_dic.values()))
    return total_count


g_dic = {11: [12, 13, 14], 14: [15, 16, 17], 17:[18, 19, 20]}
count_no_of_items_dict(g_dic)
