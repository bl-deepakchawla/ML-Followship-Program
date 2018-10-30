def pr_ace_after_ace_draw(l_ace_cards, l_total_cards):
    l_pr_ace_card = (l_ace_cards/l_total_cards) * 100
    return l_pr_ace_card


g_total_cards = 52
g_ace_draw = 1
g_total_cards = g_total_cards - g_ace_draw
g_ace_cards = 4 - g_ace_draw
g_pr_ace_card = pr_ace_after_ace_draw(g_ace_cards, g_total_cards)
print("Probability of the ace cards after drawing a ace from the packed card is", g_pr_ace_card, "%")
