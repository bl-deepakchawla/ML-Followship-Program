# Tuples are immutable we can't add or delete or update any value to/from it.
# To solve that problem we can convert tuple to list and then back changes in it and back to tuple.


def remove_tuple_value():
    tuple_value = (12, 13, 14, 15, 16)
    print("Tuple values before removing item from it", tuple_value)
    list_tuple_value = list(tuple_value)
    list_tuple_value.pop()
    tuple_value = tuple(list_tuple_value)
    print("Tuple values after removing item from it", tuple_value)


remove_tuple_value()

