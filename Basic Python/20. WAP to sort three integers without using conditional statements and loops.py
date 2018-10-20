def sort_three_integers(a, b, c):
    new_c = max(a, b, c)
    new_a = min(a, b, c)
    new_b = sum([a, b, c]) - (new_a + new_c)
    print(new_a, new_b, new_c)


x = 9
y = 1
z = 0
sort_three_integers(x, y, z)