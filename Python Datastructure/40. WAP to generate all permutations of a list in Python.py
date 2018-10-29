import itertools


def list_permutations():
    list_value = [1, 2, 3]
    perms_list_value = list(itertools.permutations(list_value))
    print("List value are", list_value)
    print("Permutations of list value", perms_list_value)


list_permutations()
