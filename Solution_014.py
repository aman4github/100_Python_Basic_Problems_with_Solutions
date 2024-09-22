# Write a Python program to find the sum of digits of a number.

num = int(input("Enter a number : "))
sum = 0

while num != 0:
    rem = num % 10
    sum = sum + rem
    num =  num // 10

print(f"Sum of digits is {sum}")