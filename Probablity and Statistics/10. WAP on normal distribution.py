def pr_normal_distribution(l_mean, l_variance, l_x):
    # We are going to use Z-score formula then look the z-score value in the z-score in the z-score table.
    # z = (x - mean ) variance
    z_score = (l_x - l_mean ) / l_variance
    return z_score


g_mean1 = 30
g_variance1 = 4
g_x1 = 40
g_z_score1 = pr_normal_distribution(g_mean1, g_variance1, g_x1)
print("Z-score of normal distribution at x < 40 is,", g_z_score1)
print("Probability of normal distribution at x < 40 is 0.9938")


g_mean1 = 30
g_variance1 = 4
g_x1 = 21
g_z_score1 = pr_normal_distribution(g_mean1, g_variance1, g_x1)
print("Z-score of normal distribution at x > 21 is,", g_z_score1)
print("Probability of normal distribution at x > 21 is 0.9878")

g_mean1 = 30
g_variance1 = 4
g_x1 = 35
g_z_score1 = pr_normal_distribution(g_mean1, g_variance1, g_x1)
print("Z-score of normal distribution at 30 < x < 35 is,", g_z_score1)
print("Probability of normal distribution at 30 < x < 35 is 0.3944")
