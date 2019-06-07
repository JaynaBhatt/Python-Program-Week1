cards = 52
aces = 4

card_drawn = 1

remaining_card = cards - card_drawn
probability1 = aces/remaining_card

remaining_aces = aces - card_drawn
probability2 = remaining_aces/cards

print(probability1*100)
print(probability2*100)
