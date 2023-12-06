with open("2023/6/input.txt") as f:
    input = f.readlines()

solve_part = 2
if solve_part == 1:
    times = [int(time) for time in input[0].split(':')[1].split()]
    distances = [int(distance) for distance in input[1].split(':')[1].split()]
else:
    times = [int(''.join(input[0].split(':')[1].split()))]
    distances = [int(''.join(input[1].split(':')[1].split()))]

win_ops_multiplied = 1
for record_time, record_distance in zip(times, distances):
    win_ops = 0
    for press_time in range(0, record_time + 1):
        boat_speed = press_time
        sail_time = record_time - press_time
        
        sail_distance = boat_speed * sail_time

        if sail_distance > record_distance:
            win_ops += 1

    if win_ops > 0:
        win_ops_multiplied *= win_ops
    
print(win_ops_multiplied)