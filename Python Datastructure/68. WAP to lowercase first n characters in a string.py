def lower_first_n_character(l_str_value, l_n_value):
    if l_n_value < len(l_str_value):
        print(l_str_value[:l_n_value].lower() + l_str_value[l_n_value:])
    else:
        print("Wrong n value it must be less than length of the string")


g_str_value = "AI IS new electricity. AI can do all things"
g_n_value = 10
lower_first_n_character(g_str_value, g_n_value)
