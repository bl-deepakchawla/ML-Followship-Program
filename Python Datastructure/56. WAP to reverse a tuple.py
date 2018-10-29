def reverse_tuple():
    tuple_value = (12, 13, 14, 15, 16)
    print("Tuple values before reverse", tuple_value)
    reversed_tuple_value = reversed(tuple_value)
    print("Tuple values after reverse", tuple(reversed_tuple_value))


reverse_tuple()
