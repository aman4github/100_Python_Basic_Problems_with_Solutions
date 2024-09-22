# Write a Python program to merge two lists.

lst1 = [10, 20, 30]
lst2 = [40, 50, 60]

# Method 1 
lst1.extend(lst2)

print(f"Marged List = {lst1}")

# Method 2 
lst1 = [10, 20, 30]
lst2 = [40, 50, 60]

print(f"Marged List = {lst1 + lst2}")

# Method 3 
lst1 = [10, 20, 30]
lst2 = [40, 50, 60]

for i in lst2:
    lst1.append(i)

print(f"Marged List = {lst1}")
