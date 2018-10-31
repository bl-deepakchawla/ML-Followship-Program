def pr_pain_pills(l_value1, l_value2, l_value3):
    l_pr_pain_pills = (l_value1 * l_value3 ) / l_value2
    return l_pr_pain_pills


g_pr_a_pain_pills = 0.10
g_pr_b_pain_pills = 0.05
g_pr_b_addict_pills = 0.08
g_pr_pain_pills = pr_pain_pills(g_pr_a_pain_pills, g_pr_b_pain_pills, g_pr_b_addict_pills)
print("Probability that they will be prescribed pain pills is", g_pr_pain_pills)
