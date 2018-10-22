def count_key(l_list_of_dic):
    count = 0
    for value in l_list_of_dic:
        if value['success']:
            count += 1
    return count


g_list_of_dic = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
         {'id': 3, 'success': True, 'name': 'Alex'}]
results = count_key(g_list_of_dic)
print("List of Dictionary values are ,", g_list_of_dic)
print("Number of success in list of dic is ,", results)
