from collections import defaultdict


with open("2023/3/input.txt") as f:
    input = f.readlines()

input = [[char for char in line.strip()] for line in input]

num_set = {'0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9'}

# Location of next char, (i, j)
dir_coord_set = {
    'n': (-1, 0),
    'ne': (-1, 1),
    'e': (0, 1),
    'se': (1, 1),
    's': (1, 0),
    'sw': (1, -1),
    'w': (0, -1),
    'nw': (-1, -1)
}

symbol_set = {'=', '$', '*', '&', '%', '#', '@', '-', '+', '/'}

# Store the sum of all of the part numbers here
sum_of_nums = 0

# Store information about the asterisks that touch the numbers;
# we need this for part two {coord:[symbol, nums]} where nums is a list of nums
symbols_nums = defaultdict(list) 

for i, line in enumerate(input):
    # Keep track of the current number
    current_num = ''
    valid_num = False

    # Also keep track of the symbols that are adjacent to the
    # current number; we need these for part two of the question
    current_num_symbols = {}

    #print(f'starting line {i}')
    for j, char in enumerate(line):
        #print(f'starting char {i}:{j}')
        if char in num_set:
            current_num += char

            # Check if the digit is adjacent to a symbol, if so
            # we can set the valid_num flag (for the full number).
            i_range = (0, len(input)-1)
            j_range = (0, len(line)-1)
            
            for dir, coord in dir_coord_set.items():
                i_next = i + coord[0]
                j_next = j + coord[1]

                # Check if we don't cross list bounds
                if (i_range[0] <= i_next <= i_range[1]) and (j_range[0] <= j_next <= j_range[1]):
                    # Check if char on coord is a 'symbol'
                    if input[i_next][j_next] in symbol_set:
                        #print(f'{i}:{j} is next to an {input[i_next][j_next]}')
                        valid_num = True

                        # Store the connection ({'3:7':'*'})
                        current_num_symbols[f'{i_next}:{j_next}'] = input[i_next][j_next]

        else:
            # The current char is not a digit; in this case
            # we want to store the current_num we kept track
            # of (if any) and only then reset current_num
            if current_num and valid_num:
                # Add the number to the grand total
                #print(f'{i}:{j}, {current_num}')
                sum_of_nums += int(current_num)   

                # Store the connection between number and symbol
                # but only if its an '*'
                for coord, symbol in current_num_symbols.items():
                    if symbol == '*':
                        symbols_nums[coord].append(current_num)

            # Reset the vars
            current_num = ''
            valid_num = False
            current_num_symbols = {}

    # At the end of iterating over a row (i); we need to check whether
    # there still is an unsaved current_num that is valid; if so,
    # we need to process it before we move to the next row, because 
    # otherwise it gets next digits on the new i appended and ugly things happen
    if current_num and valid_num:
        #print(f'{i}:{j}, {current_num}')
        sum_of_nums += int(current_num) 

        #print(current_num_symbols)
        for coord, symbol in current_num_symbols.items():
            if symbol == '*':
                symbols_nums[coord].append(current_num)


    current_num = ''
    valid_num = False
    current_num_symbols = {}

# Compute the gear ratio sum
gear_ratio_sum = 0
for coord, nums in symbols_nums.items():
    # Only if the coord has precisely 2 numbers, it is a gear
    if len(nums) == 2:
        gear_ratio = int(nums[0]) * int(nums[1])
        gear_ratio_sum += gear_ratio

print(sum_of_nums)

#print(symbols_nums)
print(gear_ratio_sum)