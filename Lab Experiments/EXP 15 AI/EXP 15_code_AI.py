# Program to demonstrate list operations

# 1. Nested List
nested_list = [1, 2, ["apple", "banana"], [10, 20, 30]]
print("Nested List:", nested_list)

# 2. Length of List
print("Length of nested_list:", len(nested_list))

# 3. Concatenation
list1 = [10, 20, 30]
list2 = [40, 50]
concat_list = list1 + list2
print("Concatenation (list1 + list2):", concat_list)

# 4. Membership
print("Is 20 in list1?", 20 in list1)
print("Is 100 in list1?", 100 in list1)

# 5. Iteration
print("Iterating through list1:")
for item in list1:
    print(item)

# 6. Indexing
print("Element at index 0 in list1:", list1[0])
print("Element at index 2 in nested_list:", nested_list[2])

# 7. Slicing
print("Slicing list1 (index 1 to 3):", list1[1:3])
print("Slicing nested_list (index 1 to end):", nested_list[1:])
