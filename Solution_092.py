# Write a Python program to find the symmetric difference between two lists.

def diff(lst1, lst2):
    lst3 = []
    for i in lst1:
        if i not in lst2:
            lst3.append(i)
    return lst3


lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
lst3 = []

lst3.append(diff(lst1, lst2))
lst3.append(diff(lst2, lst1))

print(f"The symmetric difference between two list is {lst3}")
