import re


with open("2023/4/input.txt") as f:
    input = f.readlines()

# First preprocess the card deck
deck = []
for card in input:
    card_parts = re.split("[:|]", card)
    card_num = card_parts[0].split()[1]
    winning = set(card_parts[1].split())
    nums = card_parts[2].split()

    # This one is the card count, or multiplier. We increase
    # it with 1 if we win another card of the sort. When we process
    # a card, we increment the total_card_count with this number and if
    # we win a new card with increase that cards count with the count of the
    # current card
    deck.append([card_num, winning, nums, 1])

# This will hold our answer
total_card_count = 0

# Keep processing cards untill the deck is empty
for i, card in enumerate(deck):
    current_card = card[0]
    current_winning = card[1]
    current_nums = card[2]
    current_count = card[3]

    # First increment the total score with the crrent card_count
    total_card_count += current_count

    hits = [num for num in current_nums if num in current_winning]

    # We need to add the count of the current card to the count of
    # the cards that we won (e.g. if we have two copies of card 1, and
    # we win card 3, we increase our count of card 3 by two)
    for j in range(len(hits)):
        deck[i + j + 1][3] += current_count

print(total_card_count)
