def water_jug():
    jug4 = 0
    jug3 = 0

    steps = []

    # Step 1: Fill 4L jug
    jug4 = 4
    steps.append((jug4, jug3))

    # Step 2: Pour 4 -> 3
    pour = min(jug4, 3 - jug3)
    jug4 -= pour
    jug3 += pour
    steps.append((jug4, jug3))

    # Step 3: Empty 3L jug
    jug3 = 0
    steps.append((jug4, jug3))

    # Step 4: Pour remaining 4 -> 3
    pour = min(jug4, 3 - jug3)
    jug4 -= pour
    jug3 += pour
    steps.append((jug4, jug3))

    # Step 5: Fill 4L jug again
    jug4 = 4
    steps.append((jug4, jug3))

    # Step 6: Pour 4 -> 3 until full
    pour = min(jug4, 3 - jug3)
    jug4 -= pour
    jug3 += pour
    steps.append((jug4, jug3))

    print("Steps to reach 2 litres:")
    for s in steps:
        print(s)

    print("\nGoal reached:", (jug4, jug3))

water_jug()
