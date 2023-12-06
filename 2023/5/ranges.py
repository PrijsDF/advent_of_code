range_start = 10
range_end = 18


source_start = 12
source_end = 16

print(f'range_start: {range_start}, range_end: {range_end}')
print(f'source_start: {source_start}, source_end: {source_end}\n')

# Option 1: full inclusion
# 6^^^^^^10#######18^^^^^22             (source: 6,22)
if range_start >= source_start and range_end <= source_end:
    print('option 1 is found')
# Option 2: range completely excluded left of the source
#        10#######18  20^^^^24          (source: 20,24)
elif range_end < source_start: # range_start < source_start and range_end < source_start:
    print('option 2 is found')
# Option 3: range completely excluded right of the source
# 6^^^8  10#######18                    (source: 6,8)
elif range_start > source_end:
    print('option 3 is found')
# Option 4: range starting included but exiting excluded from the source
#     8^^10###16##18                    (source: 8,16)
elif range_start >= source_start and range_end > source_end:
    print('option 4 is found')
# Option 5: range starting excluded from the source but exiting included in the source
#        10#12#####18^^^^24             (source: 12,24)
elif range_start < source_start and range_end <= source_end:
    print('option 5 is found')
# Option 6: range completely overlaps the source and exits excluding at both sides
#        10#12##16#18                   (source: 12,16)   
elif range_start < source_start and range_end > source_end:
    print('option 6 is found')
























# Scenario 1: range_start kleiner dan source_start, range_end kleiner dan source_start
# Scenario 2: range_start kleiner dan source_start, range_end groter dan source_start, range_end kleiner dan of gelijk aan source_end
# Scenario 3: range_start kleiner dan source_start, range_end groter dan source_end
# Scenario 4: range_start gelijk aan of groter dan source_start, range_end kleiner dan of gelijk aan source_end
# Scenario 5: range_start gelijk aan of groter dan source_start, range_start kleiner dan of gelirange_end groter dan source_end
# Scenario 6: range_start gelijk aan of groter dan source  