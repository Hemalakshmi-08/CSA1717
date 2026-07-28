from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Frontiers for forward and backward search
    front_start = deque([[start]])
    front_goal = deque([[goal]])

    # Visited sets
    visited_start = {start}
    visited_goal = {goal}

    while front_start and front_goal:

        # ---- Expand from start side ----
        path_start = front_start.popleft()
        node_start = path_start[-1]

        for neighbor in graph[node_start]:
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                new_path = path_start + [neighbor]
                front_start.append(new_path)

                # Meeting point found
                if neighbor in visited_goal:
                    # Find the matching path from goal side
                    for p in front_goal:
                        if p[-1] == neighbor:
                            return new_path + p[-2::-1]

        # ---- Expand from goal side ----
        path_goal = front_goal.popleft()
        node_goal = path_goal[-1]

        for neighbor in graph[node_goal]:
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                new_path = path_goal + [neighbor]
                front_goal.append(new_path)

                # Meeting point found
                if neighbor in visited_start:
                    # Find the matching path from start side
                    for p in front_start:
                        if p[-1] == neighbor:
                            return p + new_path[-2::-1]

    return None


# -----------------------------
# Example bidirectional graph
# -----------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

path = bidirectional_search(graph, 'A', 'G')
print("Path found:", path)

