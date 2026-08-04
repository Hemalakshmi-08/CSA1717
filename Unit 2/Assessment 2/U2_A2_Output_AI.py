Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: C:\Users\hemal\OneDrive\Documents\SIMATS\AI\AI_PY\U2_A2_SourceCode_AI.py

=== 1. GREEDY BEST-FIRST SEARCH (DRONE) ===
Visiting: (0, 0)
  Considering neighbor (1, 2) with h=2.24, cost=3
  Considering neighbor (2, 1) with h=2.24, cost=4
Visiting: (1, 2)
  Considering neighbor (3, 3) with h=0.00, cost=2
Visiting: (3, 3)
Goal reached by Greedy!

=== 1. A* SEARCH (DRONE) ===
Visiting: (0, 0) with g=0.00, h=4.24, f=4.24
  Checking neighbor (1, 2) with tentative g=3.00
    Updating (1, 2): g=3.00, f=5.24
  Checking neighbor (2, 1) with tentative g=4.00
    Updating (2, 1): g=4.00, f=6.24
Visiting: (1, 2) with g=3.00, h=2.24, f=5.24
  Checking neighbor (3, 3) with tentative g=5.00
    Updating (3, 3): g=5.00, f=5.00
Visiting: (3, 3) with g=5.00, h=0.00, f=5.00
Goal reached by A*!

=== 2. HILL CLIMBING (TRAFFIC) ===
Initial state x=7.39, f=19.30
Step 0: current x=7.39, f=19.30
  Neighbor x=7.05, f=20.82
  Moving to better neighbor
Step 1: current x=7.05, f=20.82
  Neighbor x=6.57, f=22.55
  Moving to better neighbor
Step 2: current x=6.57, f=22.55
  Neighbor x=7.47, f=18.88
  Staying at current state
Step 3: current x=6.57, f=22.55
  Neighbor x=7.47, f=18.90
  Staying at current state
Step 4: current x=6.57, f=22.55
  Neighbor x=5.96, f=24.07
  Moving to better neighbor
Step 5: current x=5.96, f=24.07
  Neighbor x=6.52, f=22.68
  Staying at current state
Step 6: current x=5.96, f=24.07
  Neighbor x=5.30, f=24.91
  Moving to better neighbor
Step 7: current x=5.30, f=24.91
  Neighbor x=5.84, f=24.29
  Staying at current state
Step 8: current x=5.30, f=24.91
  Neighbor x=6.25, f=23.44
  Staying at current state
Step 9: current x=5.30, f=24.91
  Neighbor x=4.93, f=25.00
  Moving to better neighbor
Step 10: current x=4.93, f=25.00
  Neighbor x=5.06, f=25.00
  Moving to better neighbor
Step 11: current x=5.06, f=25.00
  Neighbor x=5.28, f=24.92
  Staying at current state
Step 12: current x=5.06, f=25.00
  Neighbor x=5.68, f=24.54
  Staying at current state
Step 13: current x=5.06, f=25.00
  Neighbor x=5.36, f=24.87
  Staying at current state
Step 14: current x=5.06, f=25.00
  Neighbor x=4.34, f=24.56
  Staying at current state
Step 15: current x=5.06, f=25.00
  Neighbor x=6.04, f=23.92
  Staying at current state
Step 16: current x=5.06, f=25.00
  Neighbor x=5.06, f=25.00
  Moving to better neighbor
Step 17: current x=5.06, f=25.00
  Neighbor x=4.49, f=24.74
  Staying at current state
Step 18: current x=5.06, f=25.00
  Neighbor x=4.46, f=24.71
  Staying at current state
Step 19: current x=5.06, f=25.00
  Neighbor x=4.95, f=25.00
  Moving to better neighbor
Step 20: current x=4.95, f=25.00
  Neighbor x=4.05, f=24.11
  Staying at current state
Step 21: current x=4.95, f=25.00
  Neighbor x=5.87, f=24.24
  Staying at current state
Step 22: current x=4.95, f=25.00
  Neighbor x=5.87, f=24.25
  Staying at current state
Step 23: current x=4.95, f=25.00
  Neighbor x=5.81, f=24.35
  Staying at current state
Step 24: current x=4.95, f=25.00
  Neighbor x=4.87, f=24.98
  Staying at current state
Step 25: current x=4.95, f=25.00
  Neighbor x=5.93, f=24.13
  Staying at current state
Step 26: current x=4.95, f=25.00
  Neighbor x=5.49, f=24.76
  Staying at current state
Step 27: current x=4.95, f=25.00
  Neighbor x=4.66, f=24.89
  Staying at current state
Step 28: current x=4.95, f=25.00
  Neighbor x=4.08, f=24.15
  Staying at current state
Step 29: current x=4.95, f=25.00
  Neighbor x=5.12, f=24.99
  Staying at current state
Step 30: current x=4.95, f=25.00
  Neighbor x=5.07, f=24.99
  Staying at current state
Step 31: current x=4.95, f=25.00
  Neighbor x=5.69, f=24.52
  Staying at current state
Step 32: current x=4.95, f=25.00
  Neighbor x=5.93, f=24.13
  Staying at current state
Step 33: current x=4.95, f=25.00
  Neighbor x=4.28, f=24.49
  Staying at current state
Step 34: current x=4.95, f=25.00
  Neighbor x=5.81, f=24.35
  Staying at current state
Step 35: current x=4.95, f=25.00
  Neighbor x=4.92, f=24.99
  Staying at current state
Step 36: current x=4.95, f=25.00
  Neighbor x=5.92, f=24.16
  Staying at current state
Step 37: current x=4.95, f=25.00
  Neighbor x=5.84, f=24.29
  Staying at current state
Step 38: current x=4.95, f=25.00
  Neighbor x=4.19, f=24.34
  Staying at current state
Step 39: current x=4.95, f=25.00
  Neighbor x=5.45, f=24.80
  Staying at current state
Step 40: current x=4.95, f=25.00
  Neighbor x=5.72, f=24.48
  Staying at current state
Step 41: current x=4.95, f=25.00
  Neighbor x=4.68, f=24.90
  Staying at current state
Step 42: current x=4.95, f=25.00
  Neighbor x=4.28, f=24.49
  Staying at current state
Step 43: current x=4.95, f=25.00
  Neighbor x=5.52, f=24.73
  Staying at current state
Step 44: current x=4.95, f=25.00
  Neighbor x=4.69, f=24.90
  Staying at current state
Step 45: current x=4.95, f=25.00
  Neighbor x=4.18, f=24.33
  Staying at current state
Step 46: current x=4.95, f=25.00
  Neighbor x=5.53, f=24.72
  Staying at current state
Step 47: current x=4.95, f=25.00
  Neighbor x=5.54, f=24.71
  Staying at current state
Step 48: current x=4.95, f=25.00
  Neighbor x=4.13, f=24.23
  Staying at current state
Step 49: current x=4.95, f=25.00
  Neighbor x=5.79, f=24.38
  Staying at current state
Final x=4.95, f=25.00

=== 2. SIMULATED ANNEALING (TRAFFIC) ===
Initial state x=9.26, f=6.81, T=100.00
Step 0: current x=9.26, f=6.81, T=100.00
  Neighbor x=9.89, f=1.05, delta=-5.77
  Accepting move
Step 1: current x=9.89, f=1.05, T=95.00
  Neighbor x=10.06, f=-0.59, delta=-1.64
  Accepting move
Step 2: current x=10.06, f=-0.59, T=90.25
  Neighbor x=10.20, f=-2.04, delta=-1.44
  Accepting move
Step 3: current x=10.20, f=-2.04, T=85.74
  Neighbor x=10.86, f=-9.38, delta=-7.35
  Accepting move
Step 4: current x=10.86, f=-9.38, T=81.45
  Neighbor x=10.50, f=-5.25, delta=4.13
  Accepting move
Step 5: current x=10.50, f=-5.25, T=77.38
  Neighbor x=10.81, f=-8.79, delta=-3.54
  Accepting move
Step 6: current x=10.81, f=-8.79, T=73.51
  Neighbor x=11.01, f=-11.10, delta=-2.30
  Accepting move
Step 7: current x=11.01, f=-11.10, T=69.83
  Neighbor x=10.75, f=-8.05, delta=3.04
  Accepting move
Step 8: current x=10.75, f=-8.05, T=66.34
  Neighbor x=11.69, f=-19.80, delta=-11.75
  Accepting move
Step 9: current x=11.69, f=-19.80, T=63.02
  Neighbor x=12.06, f=-24.80, delta=-5.00
  Accepting move
Step 10: current x=12.06, f=-24.80, T=59.87
  Neighbor x=11.96, f=-23.39, delta=1.41
  Accepting move
Step 11: current x=11.96, f=-23.39, T=56.88
  Neighbor x=11.44, f=-16.54, delta=6.86
  Accepting move
Step 12: current x=11.44, f=-16.54, T=54.04
  Neighbor x=11.05, f=-11.66, delta=4.88
  Accepting move
Step 13: current x=11.05, f=-11.66, T=51.33
  Neighbor x=11.00, f=-11.03, delta=0.63
  Accepting move
Step 14: current x=11.00, f=-11.03, T=48.77
  Neighbor x=10.87, f=-9.41, delta=1.61
  Accepting move
Step 15: current x=10.87, f=-9.41, T=46.33
  Neighbor x=10.21, f=-2.15, delta=7.26
  Accepting move
Step 16: current x=10.21, f=-2.15, T=44.01
  Neighbor x=11.20, f=-13.47, delta=-11.32
  Rejecting move
Step 17: current x=10.21, f=-2.15, T=41.81
  Neighbor x=10.54, f=-5.66, delta=-3.50
  Accepting move
Step 18: current x=10.54, f=-5.66, T=39.72
  Neighbor x=10.98, f=-10.73, delta=-5.07
  Accepting move
Step 19: current x=10.98, f=-10.73, T=37.74
  Neighbor x=10.37, f=-3.86, delta=6.87
  Accepting move
Step 20: current x=10.37, f=-3.86, T=35.85
  Neighbor x=9.53, f=4.47, delta=8.33
  Accepting move
Step 21: current x=9.53, f=4.47, T=34.06
  Neighbor x=8.76, f=10.86, delta=6.39
  Accepting move
Step 22: current x=8.76, f=10.86, T=32.35
  Neighbor x=8.59, f=12.10, delta=1.25
  Accepting move
Step 23: current x=8.59, f=12.10, T=30.74
  Neighbor x=7.71, f=17.67, delta=5.57
  Accepting move
Step 24: current x=7.71, f=17.67, T=29.20
  Neighbor x=7.10, f=20.60, delta=2.93
  Accepting move
Step 25: current x=7.10, f=20.60, T=27.74
  Neighbor x=6.73, f=22.01, delta=1.41
  Accepting move
Step 26: current x=6.73, f=22.01, T=26.35
  Neighbor x=6.66, f=22.26, delta=0.24
  Accepting move
Step 27: current x=6.66, f=22.26, T=25.03
  Neighbor x=6.78, f=21.84, delta=-0.42
  Accepting move
Step 28: current x=6.78, f=21.84, T=23.78
  Neighbor x=7.10, f=20.60, delta=-1.24
  Accepting move
Step 29: current x=7.10, f=20.60, T=22.59
  Neighbor x=8.05, f=15.70, delta=-4.90
  Rejecting move
Step 30: current x=7.10, f=20.60, T=21.46
  Neighbor x=6.55, f=22.59, delta=1.99
  Accepting move
Step 31: current x=6.55, f=22.59, T=20.39
  Neighbor x=6.43, f=22.95, delta=0.36
  Accepting move
Step 32: current x=6.43, f=22.95, T=19.37
  Neighbor x=7.03, f=20.86, delta=-2.09
  Accepting move
Step 33: current x=7.03, f=20.86, T=18.40
  Neighbor x=7.35, f=19.49, delta=-1.38
  Rejecting move
Step 34: current x=7.03, f=20.86, T=17.48
  Neighbor x=6.74, f=21.99, delta=1.12
  Accepting move
Step 35: current x=6.74, f=21.99, T=16.61
  Neighbor x=5.74, f=24.45, delta=2.47
  Accepting move
Step 36: current x=5.74, f=24.45, T=15.78
  Neighbor x=5.69, f=24.53, delta=0.08
  Accepting move
Step 37: current x=5.69, f=24.53, T=14.99
  Neighbor x=6.32, f=23.26, delta=-1.27
  Accepting move
Step 38: current x=6.32, f=23.26, T=14.24
  Neighbor x=5.75, f=24.44, delta=1.19
  Accepting move
Step 39: current x=5.75, f=24.44, T=13.53
  Neighbor x=5.51, f=24.74, delta=0.30
  Accepting move
Step 40: current x=5.51, f=24.74, T=12.85
  Neighbor x=5.48, f=24.77, delta=0.03
  Accepting move
Step 41: current x=5.48, f=24.77, T=12.21
  Neighbor x=4.59, f=24.83, delta=0.06
  Accepting move
Step 42: current x=4.59, f=24.83, T=11.60
  Neighbor x=4.39, f=24.63, delta=-0.20
  Accepting move
Step 43: current x=4.39, f=24.63, T=11.02
  Neighbor x=4.65, f=24.88, delta=0.24
  Accepting move
Step 44: current x=4.65, f=24.88, T=10.47
  Neighbor x=4.04, f=24.08, delta=-0.80
  Accepting move
Step 45: current x=4.04, f=24.08, T=9.94
  Neighbor x=4.46, f=24.71, delta=0.63
  Accepting move
Step 46: current x=4.46, f=24.71, T=9.45
  Neighbor x=4.90, f=24.99, delta=0.28
  Accepting move
Step 47: current x=4.90, f=24.99, T=8.97
  Neighbor x=3.97, f=23.93, delta=-1.06
  Accepting move
Step 48: current x=3.97, f=23.93, T=8.53
  Neighbor x=4.30, f=24.51, delta=0.58
  Accepting move
Step 49: current x=4.30, f=24.51, T=8.10
  Neighbor x=5.06, f=25.00, delta=0.49
  Accepting move
Step 50: current x=5.06, f=25.00, T=7.69
  Neighbor x=5.31, f=24.91, delta=-0.09
  Accepting move
Step 51: current x=5.31, f=24.91, T=7.31
  Neighbor x=6.29, f=23.35, delta=-1.56
  Rejecting move
Step 52: current x=5.31, f=24.91, T=6.94
  Neighbor x=5.94, f=24.12, delta=-0.78
  Accepting move
Step 53: current x=5.94, f=24.12, T=6.60
  Neighbor x=6.27, f=23.39, delta=-0.73
  Accepting move
Step 54: current x=6.27, f=23.39, T=6.27
  Neighbor x=5.31, f=24.90, delta=1.51
  Accepting move
Step 55: current x=5.31, f=24.90, T=5.95
  Neighbor x=4.55, f=24.80, delta=-0.11
  Accepting move
Step 56: current x=4.55, f=24.80, T=5.66
  Neighbor x=5.06, f=25.00, delta=0.20
  Accepting move
Step 57: current x=5.06, f=25.00, T=5.37
  Neighbor x=5.12, f=24.99, delta=-0.01
  Accepting move
Step 58: current x=5.12, f=24.99, T=5.10
  Neighbor x=4.84, f=24.97, delta=-0.01
  Accepting move
Step 59: current x=4.84, f=24.97, T=4.85
  Neighbor x=5.56, f=24.68, delta=-0.29
  Accepting move
Step 60: current x=5.56, f=24.68, T=4.61
  Neighbor x=6.36, f=23.16, delta=-1.53
  Rejecting move
Step 61: current x=5.56, f=24.68, T=4.38
  Neighbor x=5.51, f=24.74, delta=0.06
  Accepting move
Step 62: current x=5.51, f=24.74, T=4.16
  Neighbor x=6.20, f=23.56, delta=-1.19
  Accepting move
Step 63: current x=6.20, f=23.56, T=3.95
  Neighbor x=6.05, f=23.89, delta=0.33
  Accepting move
Step 64: current x=6.05, f=23.89, T=3.75
  Neighbor x=6.92, f=21.30, delta=-2.58
  Accepting move
Step 65: current x=6.92, f=21.30, T=3.56
  Neighbor x=7.51, f=18.71, delta=-2.59
  Rejecting move
Step 66: current x=6.92, f=21.30, T=3.39
  Neighbor x=7.25, f=19.92, delta=-1.39
  Accepting move
Step 67: current x=7.25, f=19.92, T=3.22
  Neighbor x=7.69, f=17.74, delta=-2.18
  Accepting move
Step 68: current x=7.69, f=17.74, T=3.06
  Neighbor x=8.39, f=13.49, delta=-4.25
  Accepting move
Step 69: current x=8.39, f=13.49, T=2.90
  Neighbor x=8.49, f=12.81, delta=-0.68
  Rejecting move
Step 70: current x=8.39, f=13.49, T=2.76
  Neighbor x=8.17, f=14.93, delta=1.44
  Accepting move
Step 71: current x=8.17, f=14.93, T=2.62
  Neighbor x=8.36, f=13.69, delta=-1.24
  Rejecting move
Step 72: current x=8.17, f=14.93, T=2.49
  Neighbor x=7.20, f=20.18, delta=5.25
  Accepting move
Step 73: current x=7.20, f=20.18, T=2.36
  Neighbor x=6.44, f=22.92, delta=2.74
  Accepting move
Step 74: current x=6.44, f=22.92, T=2.25
  Neighbor x=7.08, f=20.69, delta=-2.23
  Rejecting move
Step 75: current x=6.44, f=22.92, T=2.13
  Neighbor x=6.49, f=22.77, delta=-0.15
  Accepting move
Step 76: current x=6.49, f=22.77, T=2.03
  Neighbor x=6.96, f=21.15, delta=-1.62
  Rejecting move
Step 77: current x=6.49, f=22.77, T=1.93
  Neighbor x=6.97, f=21.11, delta=-1.66
  Rejecting move
Step 78: current x=6.49, f=22.77, T=1.83
  Neighbor x=6.17, f=23.62, delta=0.85
  Accepting move
Step 79: current x=6.17, f=23.62, T=1.74
  Neighbor x=5.41, f=24.83, delta=1.21
  Accepting move
Step 80: current x=5.41, f=24.83, T=1.65
  Neighbor x=6.22, f=23.52, delta=-1.32
  Rejecting move
Step 81: current x=5.41, f=24.83, T=1.57
  Neighbor x=5.44, f=24.80, delta=-0.03
  Accepting move
Step 82: current x=5.44, f=24.80, T=1.49
  Neighbor x=5.43, f=24.81, delta=0.01
  Accepting move
Step 83: current x=5.43, f=24.81, T=1.42
  Neighbor x=4.63, f=24.86, delta=0.05
  Accepting move
Step 84: current x=4.63, f=24.86, T=1.35
  Neighbor x=4.25, f=24.44, delta=-0.42
  Accepting move
Step 85: current x=4.25, f=24.44, T=1.28
  Neighbor x=4.12, f=24.22, delta=-0.22
  Accepting move
Step 86: current x=4.12, f=24.22, T=1.21
  Neighbor x=3.24, f=21.90, delta=-2.32
  Rejecting move
Step 87: current x=4.12, f=24.22, T=1.15
  Neighbor x=3.15, f=21.58, delta=-2.64
  Rejecting move
Step 88: current x=4.12, f=24.22, T=1.10
  Neighbor x=4.21, f=24.37, delta=0.15
  Accepting move
Step 89: current x=4.21, f=24.37, T=1.04
  Neighbor x=4.46, f=24.71, delta=0.33
  Accepting move
Step 90: current x=4.46, f=24.71, T=0.99
  Neighbor x=4.03, f=24.05, delta=-0.66
  Rejecting move
Step 91: current x=4.46, f=24.71, T=0.94
  Neighbor x=4.65, f=24.88, delta=0.17
  Accepting move
Step 92: current x=4.65, f=24.88, T=0.89
  Neighbor x=4.48, f=24.72, delta=-0.15
  Rejecting move
Step 93: current x=4.65, f=24.88, T=0.85
  Neighbor x=5.41, f=24.83, delta=-0.04
  Accepting move
Step 94: current x=5.41, f=24.83, T=0.81
  Neighbor x=5.95, f=24.09, delta=-0.74
  Rejecting move
Step 95: current x=5.41, f=24.83, T=0.77
  Neighbor x=4.86, f=24.98, delta=0.15
  Accepting move
Step 96: current x=4.86, f=24.98, T=0.73
  Neighbor x=4.63, f=24.87, delta=-0.11
  Accepting move
Step 97: current x=4.63, f=24.87, T=0.69
  Neighbor x=4.68, f=24.90, delta=0.03
  Accepting move
Step 98: current x=4.68, f=24.90, T=0.66
  Neighbor x=3.73, f=23.38, delta=-1.52
  Rejecting move
Step 99: current x=4.68, f=24.90, T=0.62
  Neighbor x=5.20, f=24.96, delta=0.06
  Accepting move
Final x=5.20, f=24.96

=== 3. LRTA* ONLINE SEARCH (MARS ROVER) ===
Start at (0, 0), goal=(2, 1)
At state (0, 0), h=2.24
  Neighbor (1, 0), cost=1+h=2.41
  Neighbor (0, 1), cost=1+h=3.00
  Updating H[(0, 0)] = 2.41
  Moving to (1, 0)
At state (1, 0), h=1.41
  Neighbor (2, 0), cost=1+h=2.00
  Updating H[(1, 0)] = 2.00
  Moving to (2, 0)
At state (2, 0), h=1.00
  Neighbor (2, 1), cost=1+h=1.00
  Updating H[(2, 0)] = 1.00
  Moving to (2, 1)
Goal (2, 1) reached by LRTA*

=== 4. CSP BACKTRACKING (EXAM TIMETABLE) ===
Trying to assign course Math
  Trying slot 1 for Math
    Slot 1 is valid for Math, assigning.
Trying to assign course Physics
  Trying slot 1 for Physics
    Slot 1 is INVALID for Physics
  Trying slot 2 for Physics
    Slot 2 is valid for Physics, assigning.
Trying to assign course Chemistry
  Trying slot 2 for Chemistry
    Slot 2 is valid for Chemistry, assigning.
Complete assignment: {'Math': 1, 'Physics': 2, 'Chemistry': 2}
Final CSP assignment: {'Math': 1, 'Physics': 2, 'Chemistry': 2}

=== 5. MINIMAX + ALPHA-BETA (GAME AI) ===
Maximizing node at depth 2, alpha=-inf, beta=inf
  Minimizing node at depth 1, alpha=-inf, beta=inf
    Leaf node value=3
    Updated min_eval=3, beta=3
    Leaf node value=5
    Updated min_eval=3, beta=3
    Leaf node value=2
    Updated min_eval=2, beta=2
  Updated max_eval=2, alpha=2
  Minimizing node at depth 1, alpha=2, beta=inf
    Leaf node value=4
    Updated min_eval=4, beta=4
    Leaf node value=6
    Updated min_eval=4, beta=4
  Updated max_eval=4, alpha=4
  Minimizing node at depth 1, alpha=4, beta=inf
    Leaf node value=7
    Updated min_eval=7, beta=7
    Leaf node value=1
    Updated min_eval=1, beta=1
    Pruning remaining children (beta=1 <= alpha=4)
  Updated max_eval=4, alpha=4
Final Minimax value: 4
