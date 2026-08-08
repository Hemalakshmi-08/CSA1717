# Program to demonstrate list methods

# Initial List
numbers = [10, 20, 30]
print("Initial List:", numbers)

# 1. append() - adds element at the end
numbers.append(40)
print("After append(40):", numbers)

# 2. insert() - adds element at a specific position
numbers.insert(1, 15)   # insert 15 at index 1
print("After insert(1, 15):", numbers)

# 3. extend() - adds multiple elements
numbers.extend([50, 60])
print("After extend([50, 60]):", numbers)

# 4. remove() - deletes a specific element
numbers.remove(30)
print("After remove(30):", numbers)

# 5. pop() - deletes element at a specific index
numbers.pop(2)   # removes element at index 2
print("After pop(2):", numbers)

# 6. del - deletes element using index
del numbers[0]   # delete first element
print("After del numbers[0]:", numbers)
