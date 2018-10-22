def add_key_to_dict(l_dict_value, l_new_key_value):
    l_dict_value.update(l_new_key_value)
    return l_dict_value


g_dict_values = {1: 1, 2: 2, 3: 3}
g_new_key_value = {4: 4}
g_update_dict_values = add_key_to_dict(g_dict_values, g_new_key_value)
print("Dictionary values before add new key value are, ", g_dict_values)
print("Dictionary values before add new key value are, ", g_update_dict_values)
