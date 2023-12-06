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

# For part 2 we first have to get all the seed values from the different ranges
range_values = [int(seed) for seed in input[0].split(':')[1].split()]
    
# We will use a list of tuples to store the seeds
seed_ranges = []
for i in range(0, len(range_values), 2):
    start_val = range_values[i]
    # Minus 1 as the start val also should be included in the range
    end_val = start_val + (range_values[i+1] - 1)

    # Create a tuple of the seeds in the range
    seed_range = (start_val, end_val + 1)

    seed_ranges.append(seed_range)

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

# We keep track of what ranges are at which layers of the almanac 
almanac_ranges = {key:[] for key in almanac}

# The final ranges are in here
almanac_ranges['final_map'] = []

# Start by adding all starting ranges to the first layer
almanac_ranges['seed-to-soil map'] = seed_ranges

next_map_map = {
    'seed-to-soil map': 'soil-to-fertilizer map', 
    'soil-to-fertilizer map': 'fertilizer-to-water map', 
    'fertilizer-to-water map': 'water-to-light map', 
    'water-to-light map': 'light-to-temperature map', 
    'light-to-temperature map': 'temperature-to-humidity map', 
    'temperature-to-humidity map': 'humidity-to-location map', 
    'humidity-to-location map': 'final_map'
}

for map, rules in almanac.items():
    if map == 'final_map':
        break
    
    print(f'Starting with map {map}')
    
    current_ranges = almanac_ranges[map].copy()
    next_map = next_map_map[map]

    while current_ranges:
        current_range = current_ranges[0]
        range_start = current_range[0]
        range_end = current_range[1]
        #print(f'Range: {range_start}, {range_end} ({map})')

        # Once the for rule block finishes we need to know whether the range was processed
        processed = False
        for rule in rules:
            rule_start = rule[1]
            rule_end = rule[1] + rule[2]
            translation = rule[0] - rule[1]

            # Note, there are two more range options that are not relevant; see the ranges.py file
            if range_start >= rule_start and range_end <= rule_end:
                # Option 1: full inclusion
                new_range = (range_start + translation, range_end + translation)
                almanac_ranges[next_map].append(new_range)
                processed = True
            elif range_start >= rule_start and range_start < rule_end and range_end > rule_end:
                #print(f'option4: {range_start}, {range_end} is in {rule_start}, {rule_end}')
                # Option 4: range starting included but exiting excluded from the source
                new_range = (range_start + translation, rule_end + translation)
                old_range = (rule_end, range_end)
                current_ranges.append(old_range)
                almanac_ranges[next_map].append(new_range)
                processed = True
            elif range_start < rule_start and range_end > rule_start and range_end <= rule_end:
                # Option 5: range starting excluded from the source but exiting included in the source
                #        10#12#####18^^^^24             (source: 12,24)
                #print(f'option 5: {range_start}, {range_end} is in {rule_start}, {rule_end}')
                new_range = (rule_start + translation, range_end + translation)
                old_range = (range_start, rule_start)
                current_ranges.append(old_range)
                almanac_ranges[next_map].append(new_range)
                processed = True
            elif range_start < rule_start and range_end > rule_end:
                # Option 6: range completely overlaps the source and exits excluding at both sides
                #        10#12##16#18                   (source: 12,16)   
                #print(f'option 6: {range_start}, {range_end} is in {rule_start}, {rule_end}')
                new_range = (rule_start + translation, rule_end + translation)
                old_range_left = (range_start, rule_start)
                old_range_right = (rule_end, range_end)
                current_ranges.append(old_range_left)
                current_ranges.append(old_range_right)
                almanac_ranges[next_map].append(new_range)
                processed = True

        if not processed:
            almanac_ranges[next_map].append(current_range)
        
        current_ranges.pop(0)


# Take final answer
print(f'final answer: {min([range[0] for range in almanac_ranges['final_map']])}')