# Write a Python program to find the sum of elements in a list.

lst = [10, 30, 90, 20, 50]

# Method 1 
print(f"Sum of all elements in this list is {sum(lst)}")

# Method 2 
total = 0

for i in lst:
    total = total + i

print(f"Sum of all elements in this list is {total}")
