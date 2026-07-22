from collections import deque

# Initial and goal states
initial = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def bfs(initial, goal):
    queue = deque()
    queue.append((initial, []))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path))

    return None

solution = bfs(initial, goal)

print("Steps to solve the 8 Puzzle:\n")
step = 1
for state in solution:
    print("Step", step)
    for row in state:
        for value in row:
            print("_" if value == 0 else value, end=" ")
        print()
    print()
    step += 1



