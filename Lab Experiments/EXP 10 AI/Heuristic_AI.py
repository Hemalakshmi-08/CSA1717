import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    # Priority queue based on heuristic value
    frontier = []
    heapq.heappush(frontier, (heuristic[start], [start]))
    visited = set()

    while frontier:
        h_val, path = heapq.heappop(frontier)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(frontier, (heuristic[neighbor], new_path))

    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}

path = greedy_best_first_search(graph, 'A', 'G', heuristic)
print("Path found using Heuristic Search:", path)
