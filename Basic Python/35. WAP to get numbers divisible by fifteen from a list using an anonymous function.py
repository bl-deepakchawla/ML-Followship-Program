def get_no_by_anonymous_function(values):
    new_values = []
    for value in values:
        temp_value = (lambda value: (value % 15 == 0))
        new_values.append(value) if temp_value(value) else False
    return new_values


values = [12, 15, 40, 45, 80]
result = get_no_by_anonymous_function(values)
print("Numbers division by 15 are ", result)
