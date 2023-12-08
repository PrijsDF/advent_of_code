input = 2
input_map = {
    1: "intro_input.txt", 
    2: "input.txt"
}
with open(f"2023/8/{input_map[input]}") as f:
    input = f.readlines()

# Parse input
steps = [*input[0].strip()]
print(steps)
node_map = {}
start_node = None
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
    if i == 2:
        start_node = current_node
    if i == len(input) - 1:
        end_node = current_node

start_node = 'AAA'
end_node = 'ZZZ'

print(start_node, end_node, node_map, steps)

# Traverse the graph using the left/right instructions
current_node = start_node
current_steps = steps.copy()
num_steps = 0
while current_node != end_node:
    if num_steps % 1000000 == 0:
        print(num_steps)

    #print(f'Current node: {current_node}, next node {node_map[current_node + current_steps[0]]}')
    #print(steps)
    current_node = node_map[current_node + current_steps[0]]
    num_steps += 1
    current_steps.pop(0)

    # Check if we have reached the final step. If we have, while not 
    # having arrived at the final node, we need to reset the steps
    if not current_steps and current_node != end_node:
        current_steps = steps.copy()

print(num_steps)