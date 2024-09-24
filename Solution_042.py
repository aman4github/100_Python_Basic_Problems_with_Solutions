# Write a Python program to remove a specified column from a matrix.


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

remove_col = 1

cols = len(matrix[0])
rows = len(matrix)

for i in matrix:
    i.pop(remove_col) # Using pop function
    # del i[remove_col] # Using del function

print(matrix)
