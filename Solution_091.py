# Write a Python program to find the common elements in three lists.

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 5, 8, 6, 7]
lst3 = [15, 98, 6, 5, 4, 3]
lst4 = []

for i in lst1:
    if i in lst2 and i in lst3:
        lst4.append(i)

print(f"Common elements in three lists are {lst4}")
