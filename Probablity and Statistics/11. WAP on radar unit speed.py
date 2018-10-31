def pr_radar_unit(l_mean, l_variance, l_x):
    # We are going to use Z-score formula then look the z-score value in the z-score in the z-score table.
    # z = (x - mean ) variance
    z_score = (l_x - l_mean ) / l_variance
    return z_score


g_mean1 = 90
g_variance1 = 10
g_x1 = 100
g_z_score1 = pr_radar_unit(g_mean1, g_variance1, g_x1)
print("Z-score of normal distribution at x < 100 is,", g_z_score1)
print("Probability of normal distribution at x < 100 is 0.1587")
