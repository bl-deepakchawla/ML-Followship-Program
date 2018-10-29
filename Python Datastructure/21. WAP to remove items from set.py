def remove_member_sets():
    set_value = set(["User1", "User2", "User3", "User4"])
    new_value = "User4"
    print("Set value before remove User4 are ", set_value)
    set_value.remove(new_value)
    print("Set value after remove User4 are ", set_value)

remove_member_sets()
