# Q1: Water Jug Problem (4-gallon & 3-gallon jugs)

def water_jug():
    four = 0   # 4-gallon jug
    three = 0  # 3-gallon jug

    steps = []

    # Step 1: Fill 3-gallon jug
    three = 3
    steps.append((four, three))

    # Step 2: Pour 3 -> 4
    four += three
    three = 0
    steps.append((four, three))

    # Step 3: Fill 3-gallon jug again
    three = 3
    steps.append((four, three))

    # Step 4: Pour from 3 -> 4 until 4 is full
    space = 4 - four
    three -= space
    four = 4
    steps.append((four, three))

    # Step 5: Empty 4-gallon jug
    four = 0
    steps.append((four, three))

    # Step 6: Pour remaining 2 gallons from 3 -> 4
    four = three
    three = 0
    steps.append((four, three))

    return steps


result = water_jug()
print("Q1: Steps to get exactly 2 gallons in the 4-gallon jug:\n")
for i, (four, three) in enumerate(result):
    print(f"Step {i+1}: 4-gallon = {four}, 3-gallon = {three}")



# Q2: Mars Rover Agent Simulation

class MarsRover:
    def __init__(self):
        self.energy = 100
        self.samples_collected = 0
        self.position = (0, 0)

    def percepts(self):
        return {
            "camera": "image data",
            "spectrometer": "chemical composition",
            "soil_sensor": "soil data",
            "temperature": -60,
            "terrain": "rocky",
            "obstacles": True
        }

    def actions(self):
        return ["move_forward", "move_backward", "turn_left", "turn_right",
                "capture_image", "drill_sample", "analyze_sample", "transmit_data"]

    def move(self, direction):
        print(f"Rover moving {direction}")
        self.energy -= 5

    def collect_sample(self):
        print("Sample collected")
        self.samples_collected += 1
        self.energy -= 10

    def performance(self):
        return {
            "energy_left": self.energy,
            "samples_collected": self.samples_collected,
            "mission_success": self.samples_collected >= 1
        }


rover = MarsRover()
print("\nQ2: Mars Rover Percepts:", rover.percepts())
print("Actions:", rover.actions())
rover.move("forward")
rover.collect_sample()
print("Performance:", rover.performance())


# Q3: 8-Queens Problem using Backtracking

N = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_queens():
    board = [-1] * N
    solutions = []

    def backtrack(col):
        if col == N:
            solutions.append(board[:])
            return
        for row in range(N):
            if is_safe(board, row, col):
                board[col] = row
                backtrack(col + 1)

    backtrack(0)
    return solutions

sol = solve_queens()
print("\nQ3: Total solutions:", len(sol))
print("First solution:", sol[0])



# Q4: OLA Cab Booking Goal-Based Agent

class Cab:
    def __init__(self, cab_type, eta):
        self.cab_type = cab_type
        self.eta = eta

def get_available_cabs():
    return [
        Cab("mini", 5),
        Cab("sedan", 3),
        Cab("micro", 7),
        Cab("prime", 2)
    ]

def book_cab(source, destination, preferred_type):
    cabs = get_available_cabs()

    if not cabs:
        return "No cabs available"

    filtered = [c for c in cabs if c.cab_type == preferred_type]

    if not filtered:
        filtered = cabs  # fallback

    best = min(filtered, key=lambda x: x.eta)

    fare = best.eta * 10  # simple fare formula

    return f"Cab booked: {best.cab_type}, ETA={best.eta} mins, Fare={fare} INR"


print("\nQ4:", book_cab("Kanchipuram", "Chennai", "sedan"))


# Q5: Uniform Cost Search (UCS) for least-cost path S -> G

import heapq

graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': []
}

def ucs(start, goal):
    pq = [(0, start, [])]  # cost, node, path
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, neighbor, path))

    return None

cost, path = ucs('S', 'G')
print("\nQ5: Least-cost path:", path)
print("Total cost:", cost)


