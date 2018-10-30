def ing_at_end(str_value):
    str_len = len(str_value)
    if str_len >= 3:
        if str_value[str_len - 3:] == 'ing':
            str_value += 'ly'
        else:
            str_value += 'ing'
    return str_value


result_str = ing_at_end('evening')
print(result_str)
