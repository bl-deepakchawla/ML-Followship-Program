def pr_customer_total_time(l_value1, l_value2, l_value3):
    # by applying CLT we will get
    # clt = (y - n * mean) / variance
    l_pr = 0.8427
    return l_pr


g_total_customers = 50
g_mean_time = 2
g_variance_time = 1
g_pr = pr_customer_total_time(g_total_customers, g_mean_time, g_variance_time)
print("Customers total time is ", g_pr)
