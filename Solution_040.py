# Write a Python program to transpose a matrix.

matrix = [[1, 2, 3], [4, 5, 6]]

rows = len(matrix)
cols = len(matrix[0])

print("Before transpose = ")
for i in matrix:
    print(i)

empty_matrix = []

for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    empty_matrix.append(new_row)

print("After transpose")
for i in empty_matrix:
    print(i)
    