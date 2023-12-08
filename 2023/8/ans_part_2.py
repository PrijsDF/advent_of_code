import math

input = 2
input_map = {
    1: "intro_input_2.txt", 
    2: "input.txt"
}
with open(f"2023/8/{input_map[input]}") as f:
    input = f.readlines()

# Parse input
steps = [*input[0].strip()]
print(steps)
node_map = {}
start_nodes = []
end_nodes = []
for i in range(2, len(input)):
    line = input[i]
    line_parts = line.split('=')
    current_node = line_parts[0].strip()
    next_nodes = line_parts[1].strip()
    left_next_node = next_nodes.split(',')[0][1:]
    right_next_node = next_nodes.split(',')[1][:-1].strip()

    node_map[f'{current_node}L'] = left_next_node
    node_map[f'{current_node}R'] = right_next_node

    # We need the start and end node to know where to start and when we are done
    if current_node[-1] == 'A':
        start_nodes.append(current_node)
    if current_node[-1] == 'Z':
        end_nodes.append(current_node)

print(f'Start nodes: {start_nodes}')#, end_nodes)#, node_map, steps)
print(f'Are there an equal number of start and end nodes? {len(start_nodes) == len(end_nodes)}')

# Traverse the graph for each start node and note the num of steps it took to 
# reach an end node. We then compute the LCM to find the solution 
# See e.g. https://www.reddit.com/r/adventofcode/comments/18dfpub/2023_day_8_part_2_why_is_spoiler_correct/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
node_steps = {}
for node in start_nodes:
    num_steps = 0
    current_node = node
    current_steps = steps.copy()
    while not current_node[-1] == 'Z':
        current_node = node_map[current_node + current_steps[0]]
        num_steps += 1
        current_steps.pop(0)

        # Check if we have reached the final step. If we have, while not 
        # having arrived at the final node, we need to reset the steps
        if not current_steps:
            current_steps = steps.copy()

        node_steps[node] = num_steps

print(node_steps)

print(math.lcm(*[step for step in node_steps.values()]))