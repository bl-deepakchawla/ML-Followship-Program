def last_part_string(l_str_value):
    print(l_str_value.rsplit('/', 1)[0])
    print(l_str_value.rsplit('-', 1)[0])


g_str_value = 'https://www.w3resource.com/python-exercises/string'
last_part_string(g_str_value)
