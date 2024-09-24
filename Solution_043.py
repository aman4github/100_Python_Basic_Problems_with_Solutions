# Write a Python program to check if a matrix is a square matrix.

matrix = [[1, 2, 3], [4, 5, 6, 11], [7, 8, 9]]
size = len(matrix[0])
flag = 0

if len(matrix) == len(matrix[0]):
    for i in matrix:
        if len(i) == size:
            continue
        else:
            flag += 1
    if flag == 0:
        print("Yes the matrix is a Square Matrix")
    else:
        print("No the matrix is not Square Matrix")
else:
    print("No the matrix is not Square Matrix")
