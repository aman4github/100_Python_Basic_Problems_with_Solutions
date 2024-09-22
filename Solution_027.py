# Write a Python program to find the difference between two lists.

lst1 = [10, 20, 30, 30]
lst2 = [40, 50]

# Method 1 
print(f"Difference between list1 and list2 = {list(set(lst1) - set(lst2))}")

# Method 2 
print(f"Difference between list1 and list2 = {list(set(lst1).difference(set(lst2)))}")

# Method 3 
lst3 = []

for i in lst1:
    if i not in lst2:
        lst3.append(i)

print(f"Difference between list1 and list2 = {lst3}")
