Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: C:/Users/hemal/OneDrive/Documents/SIMATS/AI/AI_PY/U2_A3_SourceCode_AI.py

==============================
Q1: A* Search Dry Run (A → G)
==============================

--- Iteration 1 ---
Current Node: A
Open List:
  A: g=0, h=7, f=7
Closed List:
Selected A with g=0, h=7, f=7

  Considering neighbor B:
    Edge cost from A to B = 2
    New g=2, h=6, f=8
  Considering neighbor C:
    Edge cost from A to C = 4
    New g=4, h=4, f=8

--- Iteration 2 ---
Current Node: B
Open List:
  B: g=2, h=6, f=8
  C: g=4, h=4, f=8
Closed List:
  A: g=0, h=7, f=7
Selected B with g=2, h=6, f=8

  Neighbor C has no better path (ignored).
  Considering neighbor D:
    Edge cost from B to D = 7
    New g=9, h=3, f=12
  Considering neighbor E:
    Edge cost from B to E = 2
    New g=4, h=2, f=6

--- Iteration 3 ---
Current Node: E
Open List:
  C: g=4, h=4, f=8
  D: g=9, h=3, f=12
  E: g=4, h=2, f=6
Closed List:
  A: g=0, h=7, f=7
  B: g=2, h=6, f=8
Selected E with g=4, h=2, f=6

  Considering neighbor G:
    Edge cost from E to G = 2
    New g=6, h=0, f=6

--- Iteration 4 ---
Current Node: G
Open List:
  C: g=4, h=4, f=8
  D: g=9, h=3, f=12
  G: g=6, h=0, f=6
Closed List:
  A: g=0, h=7, f=7
  B: g=2, h=6, f=8
  E: g=4, h=2, f=6
Selected G with g=6, h=0, f=6

Goal G reached.

=== Final Result (Q1) ===
Optimal Path: A → B → E → G
Total Path Cost: 6
==============================


======================================
Q2: Minimax with Alpha-Beta Dry Run
======================================

Root: MAX
MAX node: alpha=-inf, beta=inf
  Exploring child L_MIN of MAX
    MIN node: alpha=-inf, beta=inf
      Exploring child 3 of MIN
        Leaf node: value=3
      Updated MIN value=3, alpha=-inf, beta=3
      Exploring child 5 of MIN
        Leaf node: value=5
      Updated MIN value=3, alpha=-inf, beta=3
      Exploring child 6 of MIN
        Leaf node: value=6
      Updated MIN value=3, alpha=-inf, beta=3
    MIN node returns 3

  Updated MAX value=3, alpha=3, beta=inf
  Exploring child R_MIN of MAX
    MIN node: alpha=3, beta=inf
      Exploring child 9 of MIN
        Leaf node: value=9
      Updated MIN value=9, alpha=3, beta=9
      Exploring child 1 of MIN
        Leaf node: value=1
      Updated MIN value=1, alpha=3, beta=1
      Pruning remaining children of MIN (beta=1 <= alpha=3)
    MIN node returns 1

  Updated MAX value=3, alpha=3, beta=inf
MAX node returns 3

=== Final Result (Q2) ===
Final Minimax Value at Root (MAX): 3
Best move for MAX: choose subtree with value 3 (Left MIN subtree)
Pruned Nodes: [2]
======================================

