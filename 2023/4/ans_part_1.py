import re


with open("2023/4/input.txt") as f:
    input = f.readlines()

total_points = 0

for card in input:
    card_parts = re.split("[:|]", card)
    winning = set(card_parts[1].split())
    nums = card_parts[2].split()

    hits = len([num for num in nums if num in winning])

    # Add the card points to the total points
    if hits > 0:
        total_points += 2 ** (hits - 1)

print(total_points)
