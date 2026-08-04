# ============================================================
# CSA17 – Assessment 3 (CO2–AT3 Dry Run Test)
# Q1: A* Search Dry Run (A → G)
# Q2: Minimax with Alpha-Beta Pruning Dry Run
# Combined in one Python file with step-by-step output
# ============================================================

import math

# ============================================================
# QUESTION 1 – A* SEARCH DRY RUN (GRAPH A→G)
# ============================================================

# Graph definition (adjacency list with costs)
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 3), ('D', 7), ('E', 2)],
    'C': [('E', 3)],
    'D': [('E', 2)],
    'E': [('G', 2)],
    'G': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'G': 0
}

def a_star_dry_run(start, goal):
    open_list = {start: (0, h[start], 0 + h[start])}  # node: (g, h, f)
    closed_list = {}
    parent = {}

    step = 1
    print("\n==============================")
    print("Q1: A* Search Dry Run (A → G)")
    print("==============================\n")

    while open_list:
        # Pick node with smallest f; tie-break by name
        current = min(open_list.items(), key=lambda x: (x[1][2], x[0]))[0]
        g_current, h_current, f_current = open_list[current]

        print(f"--- Iteration {step} ---")
        print(f"Current Node: {current}")
        print("Open List:")
        for node, (g_n, h_n, f_n) in open_list.items():
            print(f"  {node}: g={g_n}, h={h_n}, f={f_n}")
        print("Closed List:")
        for node, (g_n, h_n, f_n) in closed_list.items():
            print(f"  {node}: g={g_n}, h={h_n}, f={f_n}")
        print(f"Selected {current} with g={g_current}, h={h_current}, f={f_current}\n")

        # Move current from open to closed
        closed_list[current] = open_list.pop(current)

        # Goal check
        if current == goal:
            print(f"Goal {goal} reached.\n")
            break

        # Expand neighbors
        for neighbor, cost in graph[current]:
            new_g = g_current + cost
            new_h = h[neighbor]
            new_f = new_g + new_h

            # If neighbor already in closed, skip
            if neighbor in closed_list:
                continue

            # If neighbor not in open or found better g
            if neighbor not in open_list or new_g < open_list[neighbor][0]:
                print(f"  Considering neighbor {neighbor}:")
                print(f"    Edge cost from {current} to {neighbor} = {cost}")
                print(f"    New g={new_g}, h={new_h}, f={new_f}")
                open_list[neighbor] = (new_g, new_h, new_f)
                parent[neighbor] = current
            else:
                print(f"  Neighbor {neighbor} has no better path (ignored).")

        print()
        step += 1

    # Reconstruct path
    path = []
    node = goal
    total_cost = closed_list[goal][0] if goal in closed_list else None
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    print("=== Final Result (Q1) ===")
    print(f"Optimal Path: {' → '.join(path)}")
    print(f"Total Path Cost: {total_cost}")
    print("==============================\n")


# ============================================================
# QUESTION 2 – MINIMAX WITH ALPHA-BETA PRUNING DRY RUN
# ============================================================

# Game tree:
#           MAX
#         /      \
#       MIN      MIN
#     / | \    / | \
#    3  5  6  9  1  2

game_tree = {
    "root": ["L_MIN", "R_MIN"],
    "L_MIN": [3, 5, 6],
    "R_MIN": [9, 1, 2]
}

def minimax_alpha_beta_dry_run():
    print("\n======================================")
    print("Q2: Minimax with Alpha-Beta Dry Run")
    print("======================================\n")

    pruned_nodes = []

    def minimax(node, depth, is_max, alpha, beta, indent=""):
        nonlocal pruned_nodes

        # Leaf node (integer)
        if isinstance(node, int):
            print(f"{indent}Leaf node: value={node}")
            return node

        # Internal node
        if is_max:
            print(f"{indent}MAX node: alpha={alpha}, beta={beta}")
            value = -float('inf')
            for child_name in game_tree[node]:
                print(f"{indent}  Exploring child {child_name} of MAX")
                child_value = minimax(child_name, depth + 1, False, alpha, beta, indent + "    ")
                value = max(value, child_value)
                alpha = max(alpha, value)
                print(f"{indent}  Updated MAX value={value}, alpha={alpha}, beta={beta}")
                if beta <= alpha:
                    print(f"{indent}  Pruning remaining children of MAX (beta={beta} <= alpha={alpha})")
                    # record pruned children
                    idx = game_tree[node].index(child_name)
                    for pruned in game_tree[node][idx+1:]:
                        pruned_nodes.append(pruned)
                    break
            print(f"{indent}MAX node returns {value}\n")
            return value
        else:
            print(f"{indent}MIN node: alpha={alpha}, beta={beta}")
            value = float('inf')
            for child in game_tree[node]:
                print(f"{indent}  Exploring child {child} of MIN")
                child_value = minimax(child, depth + 1, True, alpha, beta, indent + "    ")
                value = min(value, child_value)
                beta = min(beta, value)
                print(f"{indent}  Updated MIN value={value}, alpha={alpha}, beta={beta}")
                if beta <= alpha:
                    print(f"{indent}  Pruning remaining children of MIN (beta={beta} <= alpha={alpha})")
                    # record pruned children
                    idx = game_tree[node].index(child)
                    for pruned in game_tree[node][idx+1:]:
                        pruned_nodes.append(pruned)
                    break
            print(f"{indent}MIN node returns {value}\n")
            return value

    # Replace leaf names with actual values
    # L_MIN children: 3,5,6 ; R_MIN children: 9,1,2
    # We already stored them as ints in game_tree.

    alpha = -float('inf')
    beta = float('inf')
    print("Root: MAX")
    final_value = minimax("root", 0, True, alpha, beta)

    print("=== Final Result (Q2) ===")
    print(f"Final Minimax Value at Root (MAX): {final_value}")
    print("Best move for MAX: choose subtree with value 3 (Left MIN subtree)")
    print(f"Pruned Nodes: {pruned_nodes}")
    print("======================================\n")


# ============================================================
# MAIN – RUN BOTH QUESTIONS
# ============================================================

if __name__ == "__main__":
    # Q1: A* Dry Run
    a_star_dry_run('A', 'G')

    # Q2: Minimax + Alpha-Beta Dry Run
    minimax_alpha_beta_dry_run()
