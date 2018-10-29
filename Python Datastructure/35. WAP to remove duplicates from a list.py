def remove_duplicate_elements_list():
    list_value = ['abc', 'xyz', 'abc', 'xyz', '1221']
    new_list_value = set()
    for value in list_value:
        if value in list_value:
            new_list_value.add(value)
    print("List value before remove duplicate elements is ", list_value)
    print("List value after remove duplicate elements is ", new_list_value)


remove_duplicate_elements_list()
