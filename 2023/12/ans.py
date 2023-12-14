from functools import cache
import time


data = 4
solve_part = 2
data_map = {
    1: "intro_input.txt", 
    2: "intro_input2.txt", 
    3: "intro_input3.txt", 
    4: "input.txt"
}
with open(f"2023/12/{data_map[data]}") as f:
    lines = f.readlines()


def is_valid_placement(springs, seq_len, i, first_seq):
    len_springs = len(springs)
    if first_seq == True and '#' in springs[:i]:
        return False
    
    #print(f'{springs}, {seq_len}')
    if i + seq_len <= len_springs:
        if not '.' in springs[i: i+seq_len]:
            if not (i - 1 >= 0 and springs[i-1] == '#'):
                if not(i + seq_len + 1 <= len_springs and springs[i+seq_len] == '#'):
                        return True

    return False


@cache
def solve_springs(springs, seq_lens, depth, i):
    count = 0
    for j in range(i, len(springs)):
        #first_seq = True if depth == 0 else False
        if is_valid_placement(springs, seq_lens[depth], j, True if depth == 0 else False):
            new_springs = springs[:j] + '#' * seq_lens[depth] + springs[j+seq_lens[depth]:]

            if depth < len(seq_lens)-1:
                count += solve_springs(new_springs, seq_lens, depth + 1, j + 1)
            else:
                new_groups = ''.join(new_springs).replace('?', '.').replace('.', ' ').split() 
                if len(new_groups) == depth+1:
                    #print(f"Final, valid sequence: {new_springs}")
                    count += 1

    return count


sum_of_num = 0
start_time = time.time()
for i, line in enumerate(lines):
    line_parts = line.strip().split()
    springs = line_parts[0]
    seq_lens = tuple(int(num) for num in line_parts[1].split(','))

    if solve_part == 2:
        springs = springs + '?' + springs + '?' + springs + '?' + springs + '?' + springs
        seq_lens *= 5

    #print(f'Starting {i+1}/{len(lines)}: {line.strip()}')
    line_start_time = time.time()
    sum_of_num += solve_springs(springs, seq_lens, 0, 0)
    print(f'Finished {i+1}/{len(lines)}: {line.strip()} in {time.time() - line_start_time:.2f} seconds')

print(f'Recursively found {sum_of_num} arrangements in {time.time() - start_time:.2f} seconds')
