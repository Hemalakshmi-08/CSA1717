from collections import deque

# BFS Function
def bfs(graph, start):
    visited = set()          # to track visited nodes
    queue = deque([start])   # queue for BFS
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        # explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting Node
start_node = 'A'

# Call BFS
bfs(graph, start_node)
