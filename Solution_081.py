# Write a Python program to find the sum of the digits of a number.

num = int(input("Enter the number : "))
sum = 0
temp = num

while num != 0:
    sum += num % 10
    num //= 10

print(f"Sum of the digits of {temp} is {sum}")
