# Program to illustrate different set operations

# Creating sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

print("Set A:", A)
print("Set B:", B)

# 1. Union
print("\nUnion (A | B):", A | B)

# 2. Intersection
print("Intersection (A & B):", A & B)

# 3. Difference
print("Difference (A - B):", A - B)
print("Difference (B - A):", B - A)

# 4. Symmetric Difference
print("Symmetric Difference (A ^ B):", A ^ B)

# 5. Membership
print("\nIs 3 in A?", 3 in A)
print("Is 10 in B?", 10 in B)

# 6. Subset / Superset
print("\nIs A subset of B?", A.issubset(B))
print("Is A superset of B?", A.issuperset(B))

# 7. Adding elements
A.add(10)
print("\nAfter adding 10 to A:", A)

# 8. Removing elements
A.remove(2)
print("After removing 2 from A:", A)

# 9. Discard (won't give error if element not present)
A.discard(100)
print("After discarding 100 (no error):", A)
