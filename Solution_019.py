# Write a Python program to find the smallest number in a list.

lst = [10, 30, 90, 20, 50]

# Method 1 
print(f"Smallest Number in this List is {min(lst)}")

# Method 2

min = lst[0] # Assuming that 1st eliment is smallest

for i in range(0, len(lst)):
    if min > lst[i]:
        min = lst[i]

print(f"Smallest number in this List is {min}")
