def built_in_documents():
    function_name = eval(input("Enter function name (without parenthesis): "))
    print("Function Name: ", function_name.__name__)
    print("Function doc: ", function_name.__doc__)
    print("Function type(builtins or user-defined): ", function_name.__module__)


built_in_documents()