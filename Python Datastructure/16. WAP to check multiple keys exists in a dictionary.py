def check_multiple_keys_dict(l_dic, l_keys):
    if all(k in l_dic for k in l_keys):
        print("Keys", l_keys, " are exists in dictionary,", l_dic)
    else:
        print("Keys", l_keys, " are not exists in dictionary,", l_dic)


g_dic = {1: 11, 2: 22, 3: 33, 4: 44}
g_kyes = (4, 3)
check_multiple_keys_dict(g_dic, g_kyes)
