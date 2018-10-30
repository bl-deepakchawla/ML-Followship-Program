def pr_ace_from_cards(l_ace_cards, l_total_cards):
    l_pr_ace_card = (l_ace_cards/l_total_cards) * 100
    return l_pr_ace_card


g_ace_cards = 4
g_total_cards = 52
g_pr_ace_card = pr_ace_from_cards(g_ace_cards, g_total_cards)
print("Probability of the ace cards from the packed cards is", g_pr_ace_card, "%")
