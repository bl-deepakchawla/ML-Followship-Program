def dict_to_table_format(l_dict):
    print('Std_id Std_Name')
    for value in l_dict.items():
        print('{}'.format(value))


g_dict = {'id120': 'ABC', 'id121': 'ABD', 'id122': 'BCD', 'id123': 'BCE'}
dict_to_table_format(g_dict)
