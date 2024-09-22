# Write a Python program to find the product of elements in a list.
import math


lst = [1, 3, 9, 2, 5]

# Method 1 
print(f"Product of all elements in this list is {math.prod(lst)}")

# Method 2 
product = 1

for i in lst:
    product = product * i

print(f"Product of all elements in this list is {product}")
