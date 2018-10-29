def remove_specific_element():
    list_value = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    list_value = [x for (index, x) in enumerate(list_value) if index not in (0, 4, 5)]
    print("List value after removing the values from the specific index value", list_value)


remove_specific_element()
