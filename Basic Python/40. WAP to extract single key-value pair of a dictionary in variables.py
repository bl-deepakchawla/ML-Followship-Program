def single_key_value_pair(g_dic_value):
    (val_1, val_2), = g_dic_value.items()
    print("Key:", val_1)
    print("Value:", val_2)


g_dic_value = {'Hello': 'World'}
single_key_value_pair(g_dic_value)
