def list_to_histrogram(list_value):
    char = ''
    for value in list_value:
        for temp in range(value):
            char += '*'
        print(char)
        char = ''


list_value = [2,3,5,4]
list_to_histrogram(list_value)
