with open("2023/2/input.txt") as f:
    input = f.readlines()

maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# Split the games and remove unnecessary punctuation
input = [line.replace(',', '').replace(';', '').strip().split(' ') for line in input]

# Store ans for part 1 of question
sum_of_ids = 0

# Store ans for part 2 of question
sum_of_powers = 0

for game in input:
    game_id = int(game[1][:-1])
    
    # Keep track of whether the game counts as valid
    valid_game = True

    # Keep track of fewest number of cubes needed 
    min_mapping = {
        'red': 0,
        'blue': 0,
        'green': 0    
    }

    # Parse the rest of the game values into a useful object
    # We still have to discard every second result though
    # (We only want results of the format ('1', 'blue'))
    for result in zip(game[2:-1], game[3:]):
        # By looking at the second item in the tuple, we automatically
        # skip the invalid results (as these wont be present in the maxes
        # mapping)
        color = result[1]
        if color in maxes:
            count = int(result[0])
            # Check if the count violates the max allowed
            if count > maxes[color]:
                valid_game = False
            
            # Update the min. required number of cubes if needed
            if count > min_mapping[color]:
                min_mapping[color] = count

    # Add the id of the game, if valid, to the sum of ids (part one of the question)
    if valid_game:
        sum_of_ids += game_id

    # Compute power of the set of min. required number of cubes
    power = min_mapping['red'] * min_mapping['blue'] * min_mapping['green'] 

    # Add the found value to the sum of powers (part two of the question)
    sum_of_powers += power

print(sum_of_ids)
print(sum_of_powers)