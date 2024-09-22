# Write a Python program to sort a list in ascending order.

lst1 = [10, 50, 20, 30, 10, 40, 50]

# Method 1 
lst1.sort()

print(f"Ascending List = {lst1}")

# Method 2 
lst2 = [10, 50, 20, 30, 10, 40, 50]

for i in range(0, len(lst2)):
    for j in range(0, len(lst2) - 1):
        if lst2[j] > lst2[j + 1]:
            temp = lst2[j]
            lst2[j] = lst2[j + 1]
            lst2[j + 1] = temp

print(f"Ascending List = {lst2}")

# Method 3 
lst3 = [10, 50, 20, 30, 10, 40, 50]

for i in range(0, len(lst3)):
    for j in range(0, len(lst3) - 1):
        if lst3[j] > lst3[j + 1]:
            lst3[j], lst3[j + 1] = lst3[j + 1], lst3[j]

print(f"Ascending List = {lst3}")
