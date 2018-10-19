def generate_list_tuple():
    values = input("Enter values in comma-separated form: ")
    list_value = values.split(',')
    tuple_value = tuple(list_value)
    print("List: ", list_value)
    print("Tuple: ", tuple_value)


generate_list_tuple()
