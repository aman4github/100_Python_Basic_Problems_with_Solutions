# Write a Python program to multiply two matrices.

def multiplication(lst1, lst2):
    lst3 = [[0, 0], [0, 0]]
    for i in range(len(lst1)):
        for j in range(len(lst1[0])):
            for k in range(len(lst1[0])):
                lst3[i][j] += lst1[i][k] * lst2[k][j]
    print(lst3)

# Consider both matrix have same row and column number
lst1 = [[1, 2], [3, 4]]
lst2 = [[5, 6], [7, 8]]

multiplication(lst1, lst2)
