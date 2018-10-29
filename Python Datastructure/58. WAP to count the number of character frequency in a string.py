def character_frequency_in_string():
    string_value = 'google.com'
    char_freq = {}
    for value in string_value:
        count_value = string_value.count(value)
        char_freq.update({value:count_value})
    print(char_freq)


character_frequency_in_string()
