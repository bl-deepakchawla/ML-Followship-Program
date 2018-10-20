def add_leading_zeros(l_str):
    print("Before leading zeros String: ", l_str)
    l_str = l_str.ljust(12, '0')
    print("After leading zeros String: ", l_str)


g_str = '14.21'
add_leading_zeros(g_str)
