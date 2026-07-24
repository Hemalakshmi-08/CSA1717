# Missionaries and Cannibals Problem
# Using Breadth-First Search (BFS)

from collections import deque

# State format: (M_left, C_left, boat_side)
# boat_side = 1 → boat on left bank
# boat_side = 0 → boat on right bank

def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    # No negative values allowed
    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False

    # Missionaries must not be outnumbered on either side
    if (M_left > 0 and M_left < C_left):
        return False
    if (M_right > 0 and M_right < C_right):
        return False

    return True


def get_successors(state):
    M_left, C_left, boat = state
    successors = []

    # Possible boat moves: (missionaries, cannibals)
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for M, C in moves:
        if boat == 1:  # boat on left bank → move people to right
            new_state = (M_left - M, C_left - C, 0)
        else:          # boat on right bank → move people to left
            new_state = (M_left + M, C_left + C, 1)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


# Initial and goal states
start_state = (3, 3, 1)
goal_state = (0, 0, 0)

solution = bfs(start_state, goal_state)

print("\n=== Missionaries & Cannibals Solution ===")
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
