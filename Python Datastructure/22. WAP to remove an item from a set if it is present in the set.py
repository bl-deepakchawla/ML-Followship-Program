def item_exists_in_sets():
    set_value = set(["User1", "User2", "User3", "User4"])
    value = "User1"
    if value in set_value:
        print(value, "present in the set", set_value)
    else:
        print(value, "not present in the set", set_value)


item_exists_in_sets()