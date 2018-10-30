def unique_words_sorted_form(l_words_list):
    l_words_list = l_words_list.split(",")
    temp = []
    [temp.append(value.replace(' ', '')) for value in l_words_list]
    sorted_list = list(set(temp))
    sorted_list.sort()
    return sorted_list


g_words_list = input("Please enter words in comma separated form")
result_words_list = unique_words_sorted_form(g_words_list)
print(result_words_list)
