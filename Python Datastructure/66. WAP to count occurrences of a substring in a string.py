def count_occurrences_substr(l_str_value, l_substr_value):
    count_value = l_str_value.count(l_substr_value)
    return count_value


g_str_value = "AI is new electricity. AI can do all things."
g_substr_value = 'AI'
g_count_value = count_occurrences_substr(g_str_value, g_substr_value)
print("String is -", g_str_value)
print("Sub-string is -", g_substr_value)
print("Total number of AI in string is -", g_count_value)
