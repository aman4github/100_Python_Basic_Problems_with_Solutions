# Write a Python program to find the sum of squares of the first n natural numbers.

sum = 0

limit = int(input("Enter the limit : "))

for i in range(1, limit+1):
    sum += (i**2)

print(f"The sum of squares of the first n natural numbers = {sum}")
