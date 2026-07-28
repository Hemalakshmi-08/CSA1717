def dfs_limited(node, goal, depth_limit, graph):
    if depth_limit == 0:
        return None
    
    if node == goal:
        return [node]
    
    for child in graph.get(node, []):
        result = dfs_limited(child, goal, depth_limit - 1, graph)
        if result is not None:
            return [node] + result
    
    return None


def iterative_deepening_search(start, goal, graph):
    depth = 0
    while True:
        print(f"Trying depth limit: {depth}")
        result = dfs_limited(start, goal, depth, graph)
        if result is not None:
            return result
        depth += 1


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

# Run IDS
path = iterative_deepening_search('A', 'G', graph)
print("Goal found! Path:", path)
