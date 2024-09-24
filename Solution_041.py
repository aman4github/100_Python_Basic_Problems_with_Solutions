# Write a Python program to find the sum of the diagonal elements of a matrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum = 0
empty_matrix = []

for i in range(len(matrix)):
    sum += matrix[i][i]
    empty_matrix.append(sum)
print(f"Diagonal Sum of this matrix = {sum}")
