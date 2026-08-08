# Program to find transpose of a matrix

# Taking matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input Matrix
print("\nEnter elements of the Matrix:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

# Transpose Logic
T = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(A[j][i])
    T.append(row)

# Display Transposed Matrix
print("\nTranspose of the Matrix:")
for i in range(cols):
    for j in range(rows):
        print(T[i][j], end=" ")
    print()
