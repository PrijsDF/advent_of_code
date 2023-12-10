import math


input = 3
input_map = {
    1: "intro_input.txt", 
    2: "intro_input_2.txt",
    3: "input.txt"
}
with open(f"2023/10/{input_map[input]}") as f:
    input = f.readlines()

# Parse input
input = [[char for char in line.strip()] for line in input]

# We need a map that specifies each direction; we will loop 
# over these for each connected pipe to try new pipes. Note that we
# only have to check those directions that would correspond to a pipe
# that can be attached to the current pipe.
dir_coord_map = {
    "n": (-1, 0),
    "e": (0, 1),
    "s": (1, 0),
    "w": (0, -1),
}

# Note; this should again be read as 'pipe |n is heading north' therefore the valid dir for |n is north
dirs_to_check_map = {
    '|n': 'n',
    '|s': 's',
    '-w': 'w',
    '-e': 'e',
    'Ln': 'n',
    'Le': 'e',
    'Jn': 'n',
    'Jw': 'w',
    '7s': 's',
    '7w': 'w',
    'Fs': 's',
    'Fe': 'e',
    'S': {'n', 's', 'w', 'e'}    
}

# We need this stupid map to translate dir + pipe to the correct name... We can however
# use this map also to validate whether the found pipe is valid
# So this map should be read for keys as (Ls) 'L was found by going s', this should be
# translated to the value (Le) 'L is heading east'
pipe_flip_map = {
    '|n': '|n',
    '|s': '|s',
    '-w': '-w',
    '-e': '-e',
    'Ls': 'Le',
    'Lw': 'Ln',
    'Js': 'Jw',
    'Je': 'Jn',
    '7n': '7w',
    '7e': '7s',
    'Fn': 'Fe',
    'Fw': 'Fs'
}

# Start following the paths from S; we have to assume that S can be anything.
# However as soon as we find a complete loop with S as its part, we can induce S
start_paths = []
# Find S and start travelling
for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char == 'S':
            for dir_to_check in dirs_to_check_map['S']:
                # We need the flipped dir to specify the subtypes
                dir_coord = dir_coord_map[dir_to_check]
                ##flipped_dir = dir_flip_map[dir_to_check]

                # Find the next pipe
                pipe_coord = (i + dir_coord[0], j + dir_coord[1])
                found_pipe = input[pipe_coord[0]][pipe_coord[1]] + dir_to_check

                # If the found pipe is valid, give its flipped name to start_paths
                if found_pipe in pipe_flip_map:
                    pipe_name = pipe_flip_map[found_pipe]
                    start_paths.append([[pipe_name, pipe_coord]])
                    #print(dir_to_check, found_pipe, pipe_coord)

finished = False
path_i = 0 
while not finished:
    current_path = start_paths[path_i]

    checked = False
    current_pipe = current_path[0]
    while not checked:
        current_pipe_name = current_pipe[0]
        current_pipe_coord = current_pipe[1]

        dir_to_check = dirs_to_check_map[current_pipe_name]
        #print(dir_to_check)
        dir_coord = dir_coord_map[dir_to_check]
        
        # Find the next pipe but only if we dont cross input boundaries
        pipe_coord = (current_pipe_coord[0] + dir_coord[0], current_pipe_coord[1] + dir_coord[1])
        found_pipe = input[pipe_coord[0]][pipe_coord[1]] + dir_to_check

        if found_pipe[0] == 'S':
            correct_path = start_paths[path_i]
            checked = True
            finished = True
        elif found_pipe in pipe_flip_map:
            pipe_name = pipe_flip_map[found_pipe]
            current_pipe = [pipe_name, pipe_coord]
            start_paths[path_i].append(current_pipe)
            #print(current_pipe)
        else:
            checked = True

    path_i += 1

print(correct_path)
print(f'Number of steps is {math.ceil(len(correct_path)/2)}')
# TODO: mogelijk is er iets nodig om subloops te vinden en daar te stoppen voor 
# paden die gevolgd worden; ik weet alleen neit zeker of dat wel mogelijk is, een 
# subloop die de hoofdloop opbreekt terwijl de hoofdloop een loop blijft