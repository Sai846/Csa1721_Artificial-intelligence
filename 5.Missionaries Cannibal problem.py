from collections import deque

class State:
    def __init__(self, left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals):
        self.left_missionaries = left_missionaries
        self.left_cannibals = left_cannibals
        self.boat = boat
        self.right_missionaries = right_missionaries
        self.right_cannibals = right_cannibals

    def is_valid(self):
        if self.left_missionaries < 0 or self.left_cannibals < 0 or self.right_missionaries < 0 or self.right_cannibals < 0:
            return False
        if self.left_missionaries > 3 or self.left_cannibals > 3 or self.right_missionaries > 3 or self.right_cannibals > 3:
            return False
        if self.left_missionaries < self.left_cannibals and self.left_missionaries > 0:
            return False
        if self.right_missionaries < self.right_cannibals and self.right_missionaries > 0:
            return False
        return True

    def is_goal(self):
        return self.left_missionaries == 0 and self.left_cannibals == 0

    def __eq__(self, other):
        return self.left_missionaries == other.left_missionaries and \
               self.left_cannibals == other.left_cannibals and \
               self.boat == other.boat and \
               self.right_missionaries == other.right_missionaries and \
               self.right_cannibals == other.right_cannibals

    def __hash__(self):
        return hash((self.left_missionaries, self.left_cannibals, self.boat, self.right_missionaries, self.right_cannibals))

    def __str__(self):
        return f"Left: {self.left_missionaries}M {self.left_cannibals}C | Boat: {'>' if self.boat else '<'} | Right: {self.right_missionaries}M {self.right_cannibals}C"


def get_neighbors(state):
    neighbors = []
    if state.boat:  # Boat is on the left side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.left_missionaries - m, state.left_cannibals - c, not state.boat,
                                      state.right_missionaries + m, state.right_cannibals + c)
                    if new_state.is_valid():
                        neighbors.append(new_state)
    else:  # Boat is on the right side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.left_missionaries + m, state.left_cannibals + c, not state.boat,
                                      state.right_missionaries - m, state.right_cannibals - c)
                    if new_state.is_valid():
                        neighbors.append(new_state)
    return neighbors


def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state.is_goal():
            return path + [current_state]
        if current_state in visited:
            continue
        visited.add(current_state)

        for neighbor_state in get_neighbors(current_state):
            if neighbor_state not in visited:
                queue.append((neighbor_state, path + [current_state]))

    return None


def print_solution(solution):
    if solution:
        print("Solution found:")
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: {state}")
    else:
        print("No solution found.")


# Example usage:
start_state = State(3, 3, True, 0, 0)  # Initial state: 3 missionaries and 3 cannibals on the left side
solution = bfs(start_state)
print_solution(solution)
