def colors_present_or_not(list_1, list_2):
    final_colors = set()
    for value in color_list_1:
        if value not in color_list_2:
            final_colors.add(value)

    return final_colors


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
final_colors = colors_present_or_not(color_list_1, color_list_2)
print(final_colors)