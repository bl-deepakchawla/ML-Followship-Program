def last(n): return n[-1]


def sorted_list_wrt_tuple_last_element():
    list_value =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print("Sorted elements wrt the tuple of last element ", sorted(list_value, key=last))


sorted_list_wrt_tuple_last_element()
