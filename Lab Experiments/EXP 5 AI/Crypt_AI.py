# Cryptarithmetic Puzzle: SEND + MORE = MONEY
# We solve by assigning digits to letters using permutations.

import itertools

def solve_crypt():
    letters = ('S','E','N','D','M','O','R','Y')
    digits = range(10)

    # S and M cannot be zero (leading digits)
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        SEND = (mapping['S']*1000 +
                mapping['E']*100 +
                mapping['N']*10 +
                mapping['D'])

        MORE = (mapping['M']*1000 +
                mapping['O']*100 +
                mapping['R']*10 +
                mapping['E'])

        MONEY = (mapping['M']*10000 +
                 mapping['O']*1000 +
                 mapping['N']*100 +
                 mapping['E']*10 +
                 mapping['Y'])

        if SEND + MORE == MONEY:
            print("Solution Found:")
            print("Mapping:", mapping)
            print(f"SEND  = {SEND}")
            print(f"MORE  = {MORE}")
            print(f"MONEY = {MONEY}")
            return

    print("No solution found.")

# Run the solver
solve_crypt()
