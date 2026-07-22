def vacuum_agent(state):
    location = state["location"]
    A = state["A"]
    B = state["B"]

    steps = []

    while A == 1 or B == 1:
        if location == "A":
            if A == 1:
                steps.append("Location A is dirty → Suck")
                A = 0
            else:
                steps.append("Location A is clean → Move to B")
                location = "B"

        elif location == "B":
            if B == 1:
                steps.append("Location B is dirty → Suck")
                B = 0
            else:
                steps.append("Location B is clean → Move to A")
                location = "A"

    steps.append("Both rooms are clean → Task complete")
    return steps


# Example initial state
state = {
    "location": "A",
    "A": 1,   # 1 = Dirty, 0 = Clean
    "B": 1
}

result = vacuum_agent(state)

print("Vacuum Cleaner Steps:\n")
for step in result:
    print(step)
