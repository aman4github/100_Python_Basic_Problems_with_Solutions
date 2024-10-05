# Write a Python program to find the sum of cubes of the first n natural numbers.

limit = int(input("Enter the number : "))
sum = 0

for i in range(1, limit+1):
    sum += i**3

print(f"Sum of cubes of first {limit} natural numbers is {sum}")
