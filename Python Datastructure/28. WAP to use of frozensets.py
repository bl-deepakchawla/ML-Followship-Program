# This function gives error that "frozenset doesn't support assignment operator."


def create_frozenset():
    set_value = frozenset(["User1", "User2", "User3"])
    set_value[1] = "User3"


create_frozenset()
