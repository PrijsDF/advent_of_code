input = 2
solve_part = 2
input_map = {
    1: "intro_input.txt", 
    2: "input.txt"
}
with open(f"2023/9/{input_map[input]}") as f:
    input = f.readlines()

sum_of_values = 0
for line in input:
    nums = [int(num) for num in line.split()]

    solved = False
    prev_diffs = [nums]
    while not solved:
        current_nums = prev_diffs[-1]
        diffs = [current_nums[i+1] - current_nums[i] for i in range(len(current_nums)-1)]
        prev_diffs.append(diffs)
        
        if all([diffs[i] == diffs[0] for i in range(1, len(diffs))]):
            # Also add a row of zeros; this makes the next steps easier
            # This row must have equal length to the last diffs row
            prev_diffs.append([0] * len(diffs))
            solved = True

    # Next we use the last num of the final sequence to find the last num of the previous sequences 
    for i in range(len(prev_diffs)-1, 0, -1):
        # For part 1 we look at the last numbers
        if solve_part == 1:
            last_num = prev_diffs[i][-1]
            # Add a new num to the previous sequence
            last_num_prev_seq = prev_diffs[i-1][-1]
            new_num = last_num_prev_seq + last_num
            prev_diffs[i-1].append(new_num)
        elif solve_part == 2:
            first_num = prev_diffs[i][0]
            # Add a new num to the previous sequence
            first_num_prev_seq = prev_diffs[i-1][0]
            new_num = first_num_prev_seq - first_num
            prev_diffs[i-1].insert(0, new_num)

    if solve_part == 1:
        sum_of_values += prev_diffs[0][-1]
    elif solve_part == 2:
        sum_of_values += prev_diffs[0][0]


print(f'The sum of the values is: {sum_of_values}')