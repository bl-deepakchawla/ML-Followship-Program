def pr_not_rainy_day_traffic_not_late(l_value1, l_value2, l_value3):
    l_pr = l_value1 * l_value2 * l_value3
    return l_pr


def pr_late(l_value1, l_value2, l_value3, l_value4):
    l_pr = l_value1 + l_value2 + l_value3 + l_value4
    return l_pr


def pr_rain_late(l_value1, l_value2):
    l_pr = l_value1 + l_value2
    l_pr = l_pr * 48/11
    return l_pr


g_pr_rainy_day = 1/3
g_pr_not_rainy_day = 2/3
g_pr_rain_traffic = 1/2
g_pr_rain_not_traffic = 1/2
g_pr_not_rain_traffic = 1/4
g_pr_not_rain_not_traffic = 3/4
g_pr_rain_traffic_late = 1/12
g_pr_rain_traffic_not_late = 1/12
g_pr_rain_not_traffic_late = 1/24
g_pr_rain_not_traffic_not_late = 1/8
g_pr_not_rain_traffic_late = 1/24
g_pr_not_rain_traffic_not_late = 1/12
g_pr_not_rain_not_traffic_late = 1/16
g_pr_not_rain_not_traffic_not_late = 7/16

g_pr1 = pr_not_rainy_day_traffic_not_late(g_pr_not_rainy_day, g_pr_not_rain_traffic, g_pr_not_rain_not_traffic)
print("Probability that it's not raining and there is heavy traffic and I am not late is", g_pr1)

g_pr2 = pr_late(g_pr_rain_traffic_late, g_pr_rain_not_traffic_late, g_pr_not_rain_traffic_late, g_pr_not_rain_not_traffic_late)
print("Probability of getting late is", g_pr2)

g_pr3 = pr_rain_late(g_pr_rain_traffic_late, g_pr_rain_not_traffic_late)
print("Probability that it rained that day is when I reached late at work", g_pr3)
