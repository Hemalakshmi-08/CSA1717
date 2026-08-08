# Program to add two matrices

# Taking matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input Matrix A
print("\nEnter elements of Matrix A:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

# Input Matrix B
print("\nEnter elements of Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)

# Adding matrices
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# Display Result
print("\nResultant Matrix (A + B):")
for i in range(rows):
    for j in range(cols):
        print(C[i][j], end=" ")
    print()
