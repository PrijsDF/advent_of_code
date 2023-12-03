with open("2023/2/input.txt") as f:
    input = f.readlines()

maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# Split the games and remove unnecessary punctuation
input = [line.replace(',', '').replace(';', '').strip().split(' ') for line in input]

sum_of_ids = 0
for game in input:
    game_id = int(game[1][:-1])
    
    # Keep track of whether the game counts as valid
    valid_game = True

    # Parse the rest of the game values into a useful object
    # We still have to discard every second result though
    # (We only want results of the format ('1', 'blue'))
    for result in zip(game[2:-1], game[3:]):
        # By look at the second item in the tuple, we automatically
        # skip the invalid results (as these wont be present in maxes)
        color = result[1]
        if color in maxes:
            count = int(result[0])
            # Check if the count violates the max allowed
            if count > maxes[color]:
                valid_game = False

    if valid_game:
        sum_of_ids += game_id

print(sum_of_ids)