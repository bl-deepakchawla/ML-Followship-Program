def longer_than_n_words_list(l_n, l_list_value):
    new_list = []
    for word in l_list_value:
        if l_n < len(word):
            new_list.append(word)
    return new_list


g_n = 5
g_list_value = ['engineer', 'testing', 'developer', 'hr', 'work', 'sales', 'marketing']
g_new_list = longer_than_n_words_list(g_n , g_list_value)
print("Words are greater then number", g_n, "in the list", g_list_value, "are ", g_new_list)
