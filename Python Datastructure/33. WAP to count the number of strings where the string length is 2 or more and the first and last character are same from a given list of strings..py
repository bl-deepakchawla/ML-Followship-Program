def count_strings():
    list_value = ['abc', 'xyz', 'aba', 'xyx', '1221']
    count = 0
    for value in list_value:
        if len(value) >=2 and value[0] == value[-1]:
            count += 1
    print("Number of strings are ", count)


count_strings()
