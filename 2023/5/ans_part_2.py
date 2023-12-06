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

# Choose whether you want to solve part one or part two:
solve_part = 2
if solve_part == 1:
    # For part 1 we simply have the list of seeds from the input
    seeds = [int(seed) for seed in input[0].split(':')[1].split()]

    # to make part 1 compatible with part two, we store the seed values
    # as if they were ranges. This is ugly but it works
    seed_ranges = [range(seed, seed+1) for seed in seeds]
else:
    # For part 2 we first have to get all the seed values from the different ranges
    range_values = [int(seed) for seed in input[0].split(':')[1].split()]
    #print(range_values)
    
    # We will use a list of generators to store the seeds
    # This list can be optimized by excluding all the duplicates that will be obtained because of
    # overlapping ranges
    seed_ranges = []

    # Use this list to see what ranges we have so far; this way we remove overlap between ranges
    current_ranges = []

    for i in range(0, len(range_values), 2):
        start_val = range_values[i]
        # Minus 1 as the start val also should be included in the range
        end_val = start_val + (range_values[i+1] - 1)
        
        #print(f'Start_val: {start_val}, end_val: {end_val}')

        # TODO; do something with the start_val and end_val depending on current_ranges contents
        # i.e. obtain new range start and end
        
        # Combine the seed set so far with the new numbers
        current_ranges.append((start_val, end_val))

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

# TODO: debug
# for key,val in almanac.items():
#     print(key)
#     print(val)

# We keep track of what ranges are at which layers of the almanac 
almanac_ranges = {key:[] for key in almanac}

# Start by adding all starting ranges to the first layer
almanac_ranges['seed-to-soil map'] = seed_ranges

next_map_map = {
    'seed-to-soil map': 'soil-to-fertilizer map', 
    'soil-to-fertilizer map': 'fertilizer-to-water map', 
    'fertilizer-to-water map': 'water-to-light map', 
    'water-to-light map': 'light-to-temperature map', 
    'light-to-temperature map': 'temperature-to-humidity map', 
    'temperature-to-humidity map': 'humidity-to-location map', 
    'humidity-to-location map': None
}

# TODO TEMP
#del almanac['fertilizer-to-water map']
del almanac['water-to-light map']
del almanac['light-to-temperature map']
del almanac['temperature-to-humidity map']
del almanac['humidity-to-location map']

for map, rules in almanac.items():
    # Fetch the ranges present for this map 
    ranges = almanac_ranges[map]
    
    next_map = next_map_map[map]
    print(almanac_ranges)
    print(ranges)
    if map != 'fertilizer-tfo-water map':
        while ranges:
            # Take the next range in the list of ranges of the current map
            range_start = ranges[0][0]
            range_end = ranges[0][1]

            processed = False

            for rule in rules: 
                dest_start = rule[0]
                source_start = rule[1]
                source_end = rule[1] + rule[2]
                range_len = rule[2]
                translation = rule[0] - rule[1]
                print(f'\nCurrent map: {map}')
                print(f'Current rule: {rule}, translation {translation}')

                print(f'range_start: {range_start}, range_end: {range_end}')
                print(f'source_start: {source_start}, source_end: {source_end}')
                
                if not processed:
                    if range_start >= source_start and range_end <= source_end:
                        # Option 1: full inclusion
                        # 6^^^^^^10#######18^^^^^22             (source: 6,22)
                        print('option 1 is found')
                        new_range = (range_start + translation, range_end + translation)
                        almanac_ranges[next_map].append(new_range)
                        processed = True
                        ranges.pop(0)
                        #print(almanac_ranges)
                    elif range_end < source_start: # range_start < source_start and range_end < source_start:
                        # Option 2: range completely excluded left of the source
                        #        10#######18  20^^^^24          (source: 20,24)
                        print('option 2 is found')
                        #almanac_ranges[next_map].append((range_start, range_end))
                        #processed = True
                    elif range_start > source_end:
                        # Option 3: range completely excluded right of the source
                        # 6^^^8  10#######18                    (source: 6,8)
                        print('option 3 is found')
                        #almanac_ranges[next_map].append((range_start, range_end))
                        #processed = True
                    elif range_start >= source_start and range_end > source_end:
                        # Option 4: range starting included but exiting excluded from the source
                        #     8^^10###16##18                    (source: 8,16)
                        print('option 4 is found')
                        new_range = (range_start + translation, source_end + translation)
                        old_range = (source_end, range_end)
                        almanac_ranges[next_map].append(new_range)
                        ranges.append(old_range)
                        ranges.pop(0)
                        processed = True
                    elif range_start < source_start and range_end <= source_end:
                        # Option 5: range starting excluded from the source but exiting included in the source
                        #        10#12#####18^^^^24             (source: 12,24)
                        print('option 5 is found')
                        new_range = (source_start + translation, range_end + translation)
                        old_range = (range_start, source_start)
                        almanac_ranges[next_map].append(new_range)
                        ranges.append(old_range)
                        ranges.pop(0)
                        processed = True
                    elif range_start < source_start and range_end > source_end:
                        # Option 6: range completely overlaps the source and exits excluding at both sides
                        #        10#12##16#18                   (source: 12,16)   
                        print('option 6 is found')
                        new_range = (source_start + translation, source_end + translation)
                        old_range_left = (range_start, source_start)
                        old_range_right = (source_end, range_end)
                        almanac_ranges[next_map].append(new_range)
                        ranges.append(old_range_left)
                        ranges.append(old_range_right)
                        ranges.pop(0)
                        processed = True
            
            # TODO: if ranges are left, they need to be sent to the next layer as is
            if not processed:
                almanac_ranges[next_map].append((range_start, range_end))
                ranges.pop(0)
                print(f'unmapped ranges: {ranges}')
            

            #ranges.pop(0)
           # if map == 'fertilizer-to-water map':
            #    break

print(almanac_ranges)
    # new_ranges = []
    # for range in seed_ranges:
    #     range_start = range[0]
    #     range_end = range[1]
    #     for rule in rules:
    #         # Only 
    #         dest_start = rule[0]
    #         source_start = rule[1]
    #         source_end = rule[1] + (rule[2])
    #         range_len = rule[2]
            
    #         # Perfect fit
    #         if source_start <= range_start and range_end <= source_end:
    #             print(f"Found perfect fit for range {range} in {rule}")
    #         # Left fit but right overflow
    #         elif source_start <= range_start and not range_end <= source_end:
    #             print(f"Found left fit for range {range} in {rule}")
    #         # right fit but left overflow
    #         elif range_end <= source_end and not source_start <= range_start:
    #             print(f"Found right fit for range {range} in {rule}")
    #         #else: 



    # seed_ranges = new_ranges

# 1/0

# if True:
#     for rule in rules:
#         dest_start = rule[0]
#         source_start = rule[1]
#         source_end = rule[1] + (rule[2] - 1)

#         if source_start <= current_num <= source_end:
#             offset = current_num - source_start

#             #print(f'hit: {current_num} in ({source_start}, {source_end}) therefore {current_num} becomes {dest_start + offset}')

#             # Update current_num with the mapped number
#             current_num = dest_start + offset


#     1/0

#     for seed in range:
#         #print(f'Current seed: {seed}')
#         current_num = seed
#         for map, rules in almanac.items():
#             # We only really need to keep looking at the rules without
#             # having to refer to the maps; when we find a rule that 
#             # matches, or none at all, we update our current_num and
#             # go to the next map. Also, we dont have to do anything
#             # if none of the maps fits; in this case current_num simply
#             # doesnt change
#             was_mapped = False
#             for rule in rules: # TODO: this is naive, we dont want to do all rules, but only as many as needed; so stop after having found the value in a rule
#                 # Only do something if we have not mapped the number yet
#                 if not was_mapped:
#                     # Note the ranges, we need to do minus 1 as the source_start also counts as a num
#                     dest_start = rule[0]
#                     source_start = rule[1]
#                     source_end = rule[1] + (rule[2] - 1)

#                     if source_start <= current_num <= source_end:
#                         offset = current_num - source_start

#                         #print(f'hit: {current_num} in ({source_start}, {source_end}) therefore {current_num} becomes {dest_start + offset}')

#                         # Update current_num with the mapped number
#                         current_num = dest_start + offset

#                         # Using this flag prevents us from possibly updating the current_num multiple times in one map 
#                         was_mapped = True
            
#             #print(f'New number after translating with {map}: {current_num}')
        
#         # The number that we are left with, is the location number. Now, 
#         # simply check whether its the lowest so far and update lowest_loc
#         if not lowest_loc or current_num < lowest_loc:
#             lowest_loc = current_num


# print(f'The lowest location number is {lowest_loc}')
