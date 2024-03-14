import heapq

# Define the goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define the moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Define a function to find the position of the empty tile
def find_empty(state):
    return state.index(0)

# Define a function to generate successor states
def successors(state):
    empty_index = find_empty(state)
    row, col = empty_index // 3, empty_index % 3
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = list(state)
            new_index = new_row * 3 + new_col
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            yield tuple(new_state)

# Define a function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_row, goal_col = (state[i] - 1) // 3, (state[i] - 1) % 3
            current_row, current_col = i // 3, i % 3
            distance += abs(goal_row - current_row) + abs(goal_col - current_col)
    return distance

# Define the A* search algorithm
def astar(start_state):
    frontier = [(manhattan_distance(start_state), start_state)]
    heapq.heapify(frontier)
    explored = set()
    
    while frontier:
        _, current_state = heapq.heappop(frontier)
        if current_state == goal_state:
            return current_state
        
        explored.add(current_state)
        for next_state in successors(current_state):
            if next_state not in explored:
                priority = manhattan_distance(next_state) + 1 # Adding 1 for each step
                heapq.heappush(frontier, (priority, next_state))

# Example usage
initial_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)  # Initial state, 0 represents the empty space
solution = astar(initial_state)
print("Solution:", solution)
