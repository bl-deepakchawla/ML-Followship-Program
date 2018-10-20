def variable_defined_or_not():
    try:
        print(a)
    except NameError:
        print("Variable a is not defined.")


variable_defined_or_not()
