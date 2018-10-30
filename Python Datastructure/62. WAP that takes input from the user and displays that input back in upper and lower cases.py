def string_lower_upper_case(l_user_str):
    lower_str = l_user_str.lower()
    upper_str = l_user_str.upper()
    return [lower_str, upper_str]


g_user_string = input("Please enter a string")
result_str = string_lower_upper_case(g_user_string)
print("Lower and upper case of your entered string are", result_str[0], result_str[1])
