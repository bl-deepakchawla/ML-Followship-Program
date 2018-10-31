import math


def correlation_coefficient(l_x, l_y):
    l_n = len(l_x)
    l_x_sum = sum(l_x)
    l_y_sum = sum(l_y)
    l_x2_sum = sum(([a*a for a in l_x]))
    l_y2_sum = sum(([a*a for a in l_y]))
    l_xy_sum = sum([a*b for a,b in zip(l_x,l_y)])
    l_numerator = (l_n * l_xy_sum - (l_x_sum * l_y_sum))
    l_denominator = math.sqrt(l_n * l_x2_sum - pow(l_x_sum,2)) * math.sqrt(l_n * l_y2_sum - pow(l_y_sum,2))
    l_cc_value = l_numerator / l_denominator
    return l_cc_value


g_x = [68, 72, 65, 70, 62, 75, 78, 64, 68]
g_y = [90, 85, 88, 100, 105, 98, 70, 65, 72]
g_cc_value = correlation_coefficient(g_x, g_y)
print("Correlation Coefficient value is ", g_cc_value)
