# Write a Python program to find the sum of odd numbers in a list.

lst = [1, 2, 3, 4, 5, 6]
sum = 0

for i in lst:
    if i % 2 != 0:
        sum += i

print(f"Sum of all odd numbers is {sum}")
