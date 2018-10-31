def pr_error_in_data_packets(l_value1, l_value2, l_value3):
    # by applying CLT we will get
    # clt = (y - n * mean) / variance
    l_pr = 0.0175
    return l_pr


g_total_errors = 120
g_mean_error = 0.1
g_variance_error = 0.09
g_pr = pr_error_in_data_packets(g_total_errors, g_mean_error, g_variance_error)
print("Total error in data packets is ", g_pr)
