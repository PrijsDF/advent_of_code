data = 1
solve_part = 1
data_map = {
    1: "intro_input.txt", 
    2: "intro_input2.txt", 
    3: "input.txt"
}
with open(f"2023/13/{data_map[data]}") as f:
    lines = f.readlines()

# Parse the input
patterns = []
current_pattern = []
for i,line in enumerate(lines):
    # If we find a line with only whitespace or the last line, then save the current pattern
    if line.isspace() or i == len(lines)-1:
        patterns.append(current_pattern)
        current_pattern = []
    else:
        current_pattern.append([char for char in line.strip()])


for pattern in patterns:
    # Need some form of recursion etc
    continue