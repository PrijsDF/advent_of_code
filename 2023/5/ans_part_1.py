import re


with open("2023/5/input.txt") as f:
    input = f.readlines()


almanac = {
    'seed-to-soil map': [],
    'soil-to-fertilizer map': [],
    'fertilizer-to-water map': [],
    'water-to-light map': [],
    'light-to-temperature map': [],
    'temperature-to-humidity map': [],
    'humidity-to-location map': []
}


# For part 1 we simply have the list of seeds from the input
seeds = [int(seed) for seed in input[0].split(':')[1].split()]

# Parse the input and fill the almanac (except for the seeds)
# Keep track of the current map 
current_map = ''
for line in input[1:]:
    line = line.strip()

    # Skip the only-whitespace lines 
    if line:
        if line.endswith(':'):
            current_map = line[:-1]
        # In this case the current line is a value of a map
        else:
            nums = [int(num) for num in line.split()]
            almanac[current_map].append(nums)

# find the location numbers; we want to find the lowest number
lowest_loc = None
for seed in seeds:
    current_num = seed
    for map, rules in almanac.items():
        # We only really need to keep looking at the rules without
        # having to refer to the maps; when we find a rule that 
        # matches, or none at all, we update our current_num and
        # go to the next map. Also, we dont have to do anything
        # if none of the maps fits; in this case current_num simply
        # doesnt change
        was_mapped = False
        for rule in rules: # TODO: this is naive, we dont want to do all rules, but only as many as needed; so stop after having found the value in a rule
            # Only do something if we have not mapped the number yet
            if not was_mapped:
                # Note the ranges, we need to do minus 1 as the source_start also counts as a num
                dest_start = rule[0]
                source_start = rule[1]
                source_end = rule[1] + (rule[2] - 1)

                if source_start <= current_num <= source_end:
                    offset = current_num - source_start

                    # Update current_num with the mapped number
                    current_num = dest_start + offset

                    # Using this flag prevents us from possibly updating the current_num multiple times in one map 
                    was_mapped = True
    
    # The number that we are left with, is the location number. Now, 
    # simply check whether its the lowest so far and update lowest_loc
    if not lowest_loc or current_num < lowest_loc:
        lowest_loc = current_num


print(f'The lowest location number is {lowest_loc}')
