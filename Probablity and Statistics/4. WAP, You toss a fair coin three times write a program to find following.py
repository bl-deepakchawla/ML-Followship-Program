def toss_event_probability(l_sample_space, l_outcome):
    l_pr = len(l_outcome) / len(l_sample_space)
    return l_pr


g_sample_space = set(['HHH', 'HHT', 'HTT', 'HTH', 'THH', 'TTT', 'TTH', 'THT'])
g_outcome1 = set(['HHH'])
g_pr1 = toss_event_probability(l_sample_space=g_sample_space, l_outcome=g_outcome1)
print("Probability of three heads (HHH) is", g_pr1)


g_outcome2 = set(['HTT', 'TTH'])
g_pr2 = toss_event_probability(l_sample_space=g_sample_space, l_outcome=g_outcome2)
print("Probability of exactly one head is", g_pr2)

g_outcome3 = set(['HHT', 'HTH', 'THH'])
g_pr3 = toss_event_probability(l_sample_space=g_sample_space, l_outcome=g_outcome3)
print("Probability of exactly one head is", g_pr3)
