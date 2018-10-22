def iterate_dict_loops(l_dict_values):
    print("Dictionary values ", l_dict_values)
    print("Display dictionary values using for loop...")
    for key in l_dict_values.keys():
        print(l_dict_values[key])


g_dict_values = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
iterate_dict_loops(g_dict_values)
