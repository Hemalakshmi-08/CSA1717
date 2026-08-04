# ============================================================
# CSA17 – Artificial Intelligence
# Combined Python Code for All 5 Questions with Step Traces
# ============================================================

import heapq
import math
import random

# ============================================================
# 1. Greedy Best-First Search & A* Search (Drone Delivery)
# ============================================================

def heuristic(a, b):
    return math.dist(a, b)

def greedy_best_first(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()
    steps = []

    while pq:
        _, node = heapq.heappop(pq)
        steps.append(f"Visiting: {node}")

        if node == goal:
            steps.append("Goal reached by Greedy!")
            return steps

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                h = heuristic(neighbor, goal)
                steps.append(f"  Considering neighbor {neighbor} with h={h:.2f}, cost={cost}")
                heapq.heappush(pq, (h, neighbor))

    steps.append("Goal not reachable by Greedy")
    return steps

def a_star(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    g_cost = {start: 0}
    steps = []

    while pq:
        _, node = heapq.heappop(pq)
        h = heuristic(node, goal)
        steps.append(f"Visiting: {node} with g={g_cost[node]:.2f}, h={h:.2f}, f={g_cost[node]+h:.2f}")

        if node == goal:
            steps.append("Goal reached by A*!")
            return steps

        for neighbor, cost in graph[node]:
            new_cost = g_cost[node] + cost
            steps.append(f"  Checking neighbor {neighbor} with tentative g={new_cost:.2f}")
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f = new_cost + heuristic(neighbor, goal)
                steps.append(f"    Updating {neighbor}: g={new_cost:.2f}, f={f:.2f}")
                heapq.heappush(pq, (f, neighbor))

    steps.append("Goal not reachable by A*")
    return steps

graph_drone = {
    (0,0): [((1,2), 3), ((2,1), 4)],
    (1,2): [((3,3), 2)],
    (2,1): [((3,3), 5)],
    (3,3): []
}

# ============================================================
# 2. Hill Climbing & Simulated Annealing (Traffic Optimization)
# ============================================================

def objective(x):
    # Simple peak at x=5
    return -(x-5)**2 + 25

def hill_climbing_trace():
    x = random.uniform(0,10)
    steps = [f"Initial state x={x:.2f}, f={objective(x):.2f}"]
    for i in range(50):
        neighbor = x + random.uniform(-1,1)
        steps.append(f"Step {i}: current x={x:.2f}, f={objective(x):.2f}")
        steps.append(f"  Neighbor x={neighbor:.2f}, f={objective(neighbor):.2f}")
        if objective(neighbor) > objective(x):
            steps.append("  Moving to better neighbor")
            x = neighbor
        else:
            steps.append("  Staying at current state")
    steps.append(f"Final x={x:.2f}, f={objective(x):.2f}")
    return steps

def simulated_annealing_trace():
    x = random.uniform(0,10)
    T = 100
    steps = [f"Initial state x={x:.2f}, f={objective(x):.2f}, T={T:.2f}"]
    for i in range(100):
        neighbor = x + random.uniform(-1,1)
        delta = objective(neighbor) - objective(x)
        steps.append(f"Step {i}: current x={x:.2f}, f={objective(x):.2f}, T={T:.2f}")
        steps.append(f"  Neighbor x={neighbor:.2f}, f={objective(neighbor):.2f}, delta={delta:.2f}")
        if delta > 0 or math.exp(delta/T) > random.random():
            steps.append("  Accepting move")
            x = neighbor
        else:
            steps.append("  Rejecting move")
        T *= 0.95
    steps.append(f"Final x={x:.2f}, f={objective(x):.2f}")
    return steps

# ============================================================
# 3. Online Search (LRTA*) – Mars Rover
# ============================================================

def lrta_star(start, goal, neighbors):
    H = {}
    current = start
    steps = [f"Start at {current}, goal={goal}"]

    def h(n):
        if n not in H:
            H[n] = heuristic(n, goal)
        return H[n]

    while current != goal:
        steps.append(f"At state {current}, h={h(current):.2f}")
        best = None
        best_cost = float('inf')

        for n in neighbors[current]:
            cost = 1 + h(n)
            steps.append(f"  Neighbor {n}, cost=1+h={cost:.2f}")
            if cost < best_cost:
                best_cost = cost
                best = n

        steps.append(f"  Updating H[{current}] = {best_cost:.2f}")
        H[current] = best_cost
        steps.append(f"  Moving to {best}")
        current = best

    steps.append(f"Goal {goal} reached by LRTA*")
    return steps

neighbors_rover = {
    (0,0): [(1,0), (0,1)],
    (1,0): [(2,0)],
    (0,1): [(1,1)],
    (1,1): [(2,1)],
    (2,0): [(2,1)],
    (2,1): []
}

# ============================================================
# 4. CSP – Exam Timetable (Backtracking + Trace)
# ============================================================

def is_valid(assignment, course, slot, constraints):
    for c, s in assignment.items():
        # same slot and common students → conflict
        if s == slot and constraints["students"][c] & constraints["students"][course]:
            return False
    return True

def backtracking_trace(courses, domains, constraints, assignment=None, steps=None):
    if assignment is None:
        assignment = {}
    if steps is None:
        steps = []

    if len(assignment) == len(courses):
        steps.append(f"Complete assignment: {assignment}")
        return assignment, steps

    course = courses[len(assignment)]
    steps.append(f"Trying to assign course {course}")

    for slot in domains[course]:
        steps.append(f"  Trying slot {slot} for {course}")
        if is_valid(assignment, course, slot, constraints):
            steps.append(f"    Slot {slot} is valid for {course}, assigning.")
            assignment[course] = slot
            result, steps = backtracking_trace(courses, domains, constraints, assignment, steps)
            if result is not None:
                return result, steps
            steps.append(f"    Backtracking from {course} at slot {slot}")
            del assignment[course]
        else:
            steps.append(f"    Slot {slot} is INVALID for {course}")
    return None, steps

courses = ["Math", "Physics", "Chemistry"]
domains = {
    "Math": [1,2],
    "Physics": [1,2],
    "Chemistry": [2,3]
}
constraints = {
    "students": {
        "Math": {"A","B"},
        "Physics": {"B","C"},
        "Chemistry": {"A"}
    }
}

# ============================================================
# 5. Minimax + Alpha-Beta Pruning (Game AI) with Trace
# ============================================================

def minimax_trace(node, depth, maximizing, alpha, beta, steps, indent=""):
    if depth == 0 or isinstance(node, int):
        steps.append(f"{indent}Leaf node value={node}")
        return node

    if maximizing:
        steps.append(f"{indent}Maximizing node at depth {depth}, alpha={alpha}, beta={beta}")
        max_eval = -float('inf')
        for child in node:
            eval = minimax_trace(child, depth-1, False, alpha, beta, steps, indent+"  ")
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            steps.append(f"{indent}  Updated max_eval={max_eval}, alpha={alpha}")
            if beta <= alpha:
                steps.append(f"{indent}  Pruning remaining children (beta={beta} <= alpha={alpha})")
                break
        return max_eval
    else:
        steps.append(f"{indent}Minimizing node at depth {depth}, alpha={alpha}, beta={beta}")
        min_eval = float('inf')
        for child in node:
            eval = minimax_trace(child, depth-1, True, alpha, beta, steps, indent+"  ")
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            steps.append(f"{indent}  Updated min_eval={min_eval}, beta={beta}")
            if beta <= alpha:
                steps.append(f"{indent}  Pruning remaining children (beta={beta} <= alpha={alpha})")
                break
        return min_eval

game_tree = [
    [3,5,2],
    [4,6],
    [7,1]
]

# ============================================================
# MAIN – RUN ALL AND PRINT STEP TRACES
# ============================================================

if __name__ == "__main__":
    # 1. Drone – Greedy & A*
    print("\n=== 1. GREEDY BEST-FIRST SEARCH (DRONE) ===")
    for s in greedy_best_first(graph_drone, (0,0), (3,3)):
        print(s)

    print("\n=== 1. A* SEARCH (DRONE) ===")
    for s in a_star(graph_drone, (0,0), (3,3)):
        print(s)

    # 2. Traffic – Hill Climbing & Simulated Annealing
    print("\n=== 2. HILL CLIMBING (TRAFFIC) ===")
    for s in hill_climbing_trace():
        print(s)

    print("\n=== 2. SIMULATED ANNEALING (TRAFFIC) ===")
    for s in simulated_annealing_trace():
        print(s)

    # 3. Mars Rover – LRTA*
    print("\n=== 3. LRTA* ONLINE SEARCH (MARS ROVER) ===")
    for s in lrta_star((0,0), (2,1), neighbors_rover):
        print(s)

    # 4. Exam Timetable – CSP
    print("\n=== 4. CSP BACKTRACKING (EXAM TIMETABLE) ===")
    result, steps_csp = backtracking_trace(courses, domains, constraints)
    for s in steps_csp:
        print(s)
    print(f"Final CSP assignment: {result}")

    # 5. Game AI – Minimax + Alpha-Beta
    print("\n=== 5. MINIMAX + ALPHA-BETA (GAME AI) ===")
    steps_mm = []
    value = minimax_trace(game_tree, 2, True, -float('inf'), float('inf'), steps_mm)
    for s in steps_mm:
        print(s)
    print(f"Final Minimax value: {value}")
