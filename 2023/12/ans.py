data = 3
solve_part = 1
data_map = {
    1: "intro_input.txt", 
    2: "intro_input2.txt", 
    3: "input.txt"
}
with open(f"2023/12/{data_map[data]}") as f:
    lines = f.readlines()


def is_valid_placement(springs, seq_len, i, first_seq):
    len_springs = len(springs)
    if first_seq == True and '#' in springs[:i]:
        return False
    
    # TODO .##.?#??.#.?# 2,1,1,1 faalt...
    #print(i, springs)
    if i + seq_len <= len_springs:
        #if letter == 'k' and i == 11:
            #print(i, seq_len, springs)
        if not '.' in springs[i: i+seq_len]:
            #if letter == 'i':
                #print(i, seq_len, springs)
            if not (i - 1 >= 0 and springs[i-1] == '#'):
                #if letter == 'k' :
                    #print(i, seq_len, springs)
                if not(i + seq_len + 1 <= len_springs and springs[i+seq_len] == '#'):
                    #if letter == 'k':
                        #print(i, seq_len, springs)
                        return True

    return False


# NEEDS BACKTRACKING>>>>><><><><><><><>>
# 6 is max len of seq_lens so it still works 
sum_of_valid_arrangements = 0
for line in lines:
    print(line, '\n')
    line_parts = line.strip().split()
    springs = [char for char in line_parts[0]]
    seq_lens = [int(num) for num in line_parts[1].split(',')]
    
    len_springs = len(springs)
    for i in range(len_springs):
        if is_valid_placement(springs, seq_lens[0], i, True):
            i_springs = springs[:i] + ['#'] * seq_lens[0] + springs[i+seq_lens[0]:]

            if len(seq_lens) == 1:
                new_groups = ''.join(i_springs).replace('?', '.').replace('.', ' ').split() 
                if len(new_groups) == 1:
                    print(f'Valid i: {i}')
                    print(''.join(i_springs))
                    sum_of_valid_arrangements += 1
            else:                  
                for j in range(i+1, len_springs):
                    if is_valid_placement(i_springs, seq_lens[1], j, False):
                        j_springs = i_springs[:j] + ['#'] * seq_lens[1] + i_springs[j+seq_lens[1]:]

                        if len(seq_lens) == 2:
                            new_groups = ''.join(j_springs).replace('?', '.').replace('.', ' ').split() 
                            if len(new_groups) == 2:
                                print(f'Valid i, j: {i}, {j}')
                                print(''.join(j_springs))
                                sum_of_valid_arrangements += 1
                        else:     
                            for k in range(j+1, len_springs):
                                if is_valid_placement(j_springs, seq_lens[2], k, False):
                                    k_springs = j_springs[:k] + ['#'] * seq_lens[2] + j_springs[k+seq_lens[2]:]

                                    if len(seq_lens) == 3:
                                        new_groups = ''.join(k_springs).replace('?', '.').replace('.', ' ').split() 
                                        if len(new_groups) == 3:
                                            print(f'Valid i, j, k: {i}, {j}, {k}')
                                            print(''.join(k_springs), '\n')
                                            sum_of_valid_arrangements += 1
                                    else:  
                                        for l in range(k+1, len_springs):
                                            if is_valid_placement(k_springs, seq_lens[3], l, False):
                                                l_springs = k_springs[:l] + ['#'] * seq_lens[3] + k_springs[l+seq_lens[3]:]

                                                if len(seq_lens) == 4:
                                                    new_groups = ''.join(l_springs).replace('?', '.').replace('.', ' ').split() 
                                                    if len(new_groups) == 4:
                                                        print(f'Valid i, j, k, l: {i}, {j}, {k}, {l}')
                                                        print(''.join(l_springs), '\n')
                                                        sum_of_valid_arrangements += 1
                                                else:                         
                                                    for m in range(l+1, len_springs):
                                                        if is_valid_placement(l_springs, seq_lens[4], m, False):
                                                            m_springs = l_springs[:m] + ['#'] * seq_lens[4] + l_springs[m+seq_lens[4]:]

                                                            if len(seq_lens) == 5:
                                                                new_groups = ''.join(m_springs).replace('?', '.').replace('.', ' ').split() 
                                                                if len(new_groups) == 5:
                                                                    print(f'Valid i, j, k, l, m: {i}, {j}, {k}, {l}, {m}')
                                                                    print(''.join(m_springs), '\n')
                                                                    sum_of_valid_arrangements += 1
                                                            else:  
                                                                for n in range(m+1, len_springs):
                                                                    if is_valid_placement(m_springs, seq_lens[5], n, False):
                                                                        n_springs = m_springs[:n] + ['#'] * seq_lens[5] + m_springs[n+seq_lens[5]:]
                                                                        
                                                                        new_groups = ''.join(n_springs).replace('?', '.').replace('.', ' ').split() 
                                                                        if len(new_groups) == 6:
                                                                            print(f'Valid i, j, k, l, m, n: {i}, {j}, {k}, {l}, {m}, {n}')
                                                                            print(''.join(n_springs), '\n')
                                                                            # Dit is de max len voor seq_lens, dus geen extra ifelse nodig
                                                                            sum_of_valid_arrangements += 1


    
print(sum_of_valid_arrangements)