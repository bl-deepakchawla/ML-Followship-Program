def pr_woman_over_50_cancer(l_value1, l_value2):
    temp = l_value1 + l_value2
    l_pr = l_value1 / temp
    return l_pr


g_pr_cancer = 0.01
g_pr_not_cancer = 0.99
g_pr_cancer_positive_test = 0.9
g_pr_not_cancer_positive_test = 0.08
g_pr_woman_cancer = pr_woman_over_50_cancer(g_pr_cancer_positive_test, g_pr_not_cancer_positive_test)