data = 1
solve_part = 2
data_map = {
    1: "intro_input.txt", 
    2: "input.txt"
}
with open(f"2023/11/{data_map[data]}") as f:
    lines = f.readlines()

# Parse input
universe = [[char for char in line.strip()] for line in lines]

# Find empty rows and cols
n_rows = len(universe)
n_cols = len(universe[0])

empty_i = [1] * n_rows
empty_j = [1] * n_cols

for i in range(n_rows):
    for j in range(n_cols):
        if universe[i][j] == '#':
            empty_i[i] = 0
            empty_j[j] = 0

# Expand the universe, first rows then cols
for i in range(len(empty_i)-1, -1, -1):
    if empty_i[i] == 1:
        universe.insert(i, ['.'] * n_cols)

# We have to reset the number of rows, as it has expanded 
n_rows = len(universe)
for j in range(len(empty_j)-1, -1, -1):
    if empty_j[j] == 1:
        for i in range(n_rows):
            universe[i].insert(j, '@')

# Reset the number of cols in case we need it
n_cols = len(universe[0])

# Find the galaxies in the expanded universe
galaxy_coords = []
# These shadow i and j will keep track of the real expansion (part two)
shadow_i = 0
shadow_j = 0
for i in range(n_rows):
    # We only want to update shadow_i once per row
    if universe[i][0] == '@':
        shadow_i += 1000000
    else:
        shadow_i += 1

    for j in range(n_cols):
        # We only want to update shadow_j once per col, so we only do the check
        # for the final element in the col
        if j == n_cols - 1 and universe[i][j] == '@':
            shadow_j += 1000000
        else:
            shadow_j += 1

        if universe[i][j] == '#':
            if solve_part == 1:
                galaxy_coords.append((i, j))
            else:
                galaxy_coords.append((shadow_i, shadow_j))

#for t in universe:
#    print(t)

# Find the distances between the galaxies
total_distance = 0
n_galaxies = len(galaxy_coords)
for i in range(n_galaxies-1):
    gala_x = galaxy_coords[i][0]
    gala_y = galaxy_coords[i][1]

    for j in range(i+1, n_galaxies):
        next_gala_x = galaxy_coords[j][0]
        next_gala_y = galaxy_coords[j][1]

        distance = abs(gala_x - next_gala_x) + abs(gala_y - next_gala_y)
        total_distance += distance

print(total_distance)