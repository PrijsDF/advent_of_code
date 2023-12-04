with open("2023/3/input.txt") as f:
    input = f.readlines()

#input = [[char for char in line.strip()][:10] for line in input[2:4]]
input = [[char for char in line.strip()] for line in input]
#input = input[:2]
# input = [[char for char in line.strip()] for line in input]

# num_set = {'0', '1', '2', '3', '4',
#            '5', '6', '7', '8', '9', '.'}

# all = [char for line in input for char in line if char not in num_set]
# print(set(all))
# 1/0
# input[0][-1] = '2'
# input[0][-2] = '3'
# input[0][-3] = '7'

# input[1][-2] = '.'

# print(input[0])
# print(input[1])

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

# Store the  sum of all of the part numbers here
sum_of_nums = 0

for i, line in enumerate(input):
    # Keep track of the current number
    current_num = ''
    valid_num = False

    #print(f'starting line {i}')
    for j, char in enumerate(line):
        #print(f'starting char {i}:{j}')
        if char in num_set:
            current_num += char

            # Check if the digit is adjacent to a symbol, if so
            # we can set the valid_num flag (for the full number).
            # We only have to do this once for a number; if we already
            # know valid_num is true, we can skip this check for the 
            # current num. Also, we need to be aware not to cross list 
            # boundaries
            if not valid_num:
                i_range = (0, len(input)-1)
                j_range = (0, len(line)-1)
                
                for dir, coord in dir_coord_set.items():
                    i_next = i + coord[0]
                    j_next = j + coord[1]

                    # Check if we don't cross list bounds
                    if (i_range[0] <= i_next <= i_range[1]) and (j_range[0] <= j_next <= j_range[1]):
                        # Check if char on coord is a 'symbol'
                        if input[i_next][j_next] in symbol_set:
                            print(f'{i}:{j} is next to an {input[i_next][j_next]}')
                            valid_num = True

        else:
            # The current char is not a digit; in this case
            # we want to store the current_num we kept track
            # of (if any) and only then reset current_num
            if current_num and valid_num:
                # Add the number to the grand total
                print(f'{i}:{j}, {current_num}')
                sum_of_nums += int(current_num)   
 
            current_num = ''
            valid_num = False

    # At the end of iterating over a row (i); we need to check whether
    # there still is an unsaved current_num that is valid; if so,
    # we need to process it before we move to the next row, because 
    # otherwise it gets next digits on the new i appended and ugly things happen
    if current_num and valid_num:
        print(f'{i}:{j}, {current_num}')
        sum_of_nums += int(current_num) 

    current_num = ''
    valid_num = False

print(sum_of_nums)