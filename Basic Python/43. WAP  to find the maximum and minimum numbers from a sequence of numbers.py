def min_max_without_using(x):
    min = max = x[0]
    for i in x[1:]:
        if i < min:
            min = i
        else:
            if i > max: max = i
    return (min,max)

print(min_max_without_using([9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19]))
print(min_max_without_using([1]))
print(min_max_without_using([2, 0, 2, 7, 5, -1, -2]))
