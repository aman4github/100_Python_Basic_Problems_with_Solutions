# Write a Python program to find the largest number in a list.

lst = [10, 30, 90, 20, 50]

# Method 1 
print(f"Largest Number in this List is {max(lst)}")

# Method 2

max = lst[0] # Assuming that 1st eliment is largest

for i in range(0, len(lst)):
    if max < lst[i]:
        max = lst[i]

print(f"Largest number in this List is {max}")
