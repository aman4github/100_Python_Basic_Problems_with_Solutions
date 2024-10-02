# Write a Python program to find the average of numbers in a list.

lst = [1, 2, 3, 4, 5, 6]
total = 0

for i in lst:
    total += i

print(f"Average of the numbers in this list is {total / len(lst)}")
