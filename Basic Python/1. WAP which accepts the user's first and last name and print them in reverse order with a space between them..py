def reverse_order():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    print("".join(reversed(fname)), "".join(reversed(lname)))


reverse_order()