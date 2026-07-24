# Travelling Salesman Problem (TSP)
# Using Brute Force approach with permutations

from itertools import permutations

# Distance matrix (example for 4 cities)
# 0 means same city, symmetric matrix
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of cities
n = len(dist_matrix)
cities = list(range(n))

# Starting city (0)
start = 0

# Initialize minimum path and cost
min_cost = float('inf')
best_path = []

# Generate all possible paths excluding start city
for perm in permutations(cities[1:]):
    path = [start] + list(perm) + [start]
    cost = 0

    # Calculate total cost for this path
    for i in range(len(path) - 1):
        cost += dist_matrix[path[i]][path[i + 1]]

    # Update minimum cost and path
    if cost < min_cost:
        min_cost = cost
        best_path = path

# Display result
print("\n=== Travelling Salesman Problem ===")
print("Shortest Path:", ' → '.join(map(str, best_path)))
print("Minimum Cost:", min_cost)
