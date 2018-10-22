def remove_key_dict(l_dict):
    l_dict.popitem()
    return l_dict


g_dict = {1: 10, 2: 20, 3: 30, 4: 40}
print("Dictionary values before remove any key is,", g_dict)
g_resultant_dict = remove_key_dict(g_dict)
print("Dictionary values after remove key ", g_resultant_dict)
