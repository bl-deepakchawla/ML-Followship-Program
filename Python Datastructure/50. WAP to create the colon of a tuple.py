from copy import deepcopy


def create_colon_tuple():
    # create a tuple
    tuplex = ("HELLO", 5, [], True)
    print(tuplex)
    # make a copy of a tuple using deepcopy() function
    tuplex_clone = deepcopy(tuplex)
    tuplex_clone[2].append(50)
    print(tuplex_clone)
    print(tuplex)


create_colon_tuple()
