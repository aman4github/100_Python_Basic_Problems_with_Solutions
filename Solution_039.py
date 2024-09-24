# Write a Python program to find the sum of elements in a matrix.

matrix = [[1, 2, 3], [4, 5, 6]]

sum = 0

for i in matrix:
    for j in i:
        sum += j

print(f"Sum of list elements is {sum}")
