with open("2023/7/input.txt") as f:
    input = f.readlines()

handbids = [line.strip().split() for line in input]

"""
Types of hands:
five of a kind 
four of a kind
full house
three of a kind
two pair
one par
high card
"""

# We use a card map to be able to sort on the hand later 
card_map = {
    "A": "a",
    "K": "b", 
    "Q": "c", 
    "J": "d", 
    "T": "e", 
    "9": "f", 
    "8": "g", 
    "7": "h", 
    "6": "i", 
    "5": "j", 
    "4": "k", 
    "3": "l", 
    "2": "m"     
}

def get_score(hand):
    """
    Types of hands:
    five of a kind == 7
    four of a kind == 6
    full house == 5
    three of a kind == 4
    two pair == 3
    one par == 2
    high card == 1
    """
    # Get the cards
    cards = {mapped_card:0 for mapped_card in card_map.values()}
    for card in hand:
        cards[card] += 1

    
    # Get the doubles
    nums_of_kinds = {
        5: 0,
        4: 0,
        3: 0,
        2: 0
    }
    for card, count in cards.items():
        if count > 1:
            nums_of_kinds[count] += 1

    # Decide on the score
    if nums_of_kinds[5] == 1:
        return 7
    elif nums_of_kinds[4] == 1:
        return 6
    elif nums_of_kinds[3] >= 1 and nums_of_kinds[2] >= 1:
        return 5
    elif nums_of_kinds[3] >= 1:
        return 4
    elif nums_of_kinds[2] >= 2:
        return 3
    elif nums_of_kinds[2] == 1:
        return 2
    else:
        return 1


# Get the scores of the hands
hand_scores = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
for i, handbid in enumerate(handbids):
    hand = ''.join([card_map[card] for card in handbid[0]])
    bid = handbid[1]
    
    score = get_score(hand)

    hand_scores[score].append([hand, bid])

# We will order per score and simply keep one final_order list which we append
# with each sorted sublist. If we start with the highest score, the final_order list
# will have the right structure
final_order = []
for score in range(7, 0, -1):
    hands_with_score = hand_scores[score]

    if hands_with_score:
        final_order += sorted(hands_with_score, key=lambda x: x[0])

len_final_order = len(final_order)
total_winnings = 0
for i, hand in enumerate(final_order):
    rank = len_final_order - i
    #print(f'{rank} * {int(final_order[i][1])} = {rank * int(final_order[i][1])}')
    total_winnings += int(final_order[i][1]) * rank

print(f'Total winnings: {total_winnings}')