def longest_word_list(l_str_list):
    str_len_list = []
    for str_value in l_str_list:
        str_len_list.append(len(str_value))
    l_long_str = max(str_len_list)
    return l_long_str


g_str_list = ['abc', 'morning', 'evening', 'night', 'lunch']
g_long_str = longest_word_list(g_str_list[:])
print("Longest string in the list of length is", g_long_str)
