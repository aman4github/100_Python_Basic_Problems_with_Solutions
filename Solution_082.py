# Write a Python program to reverse the digits of a number.

num = int(input("Enter a number : "))
sum = 0
temp = num

while num != 0:
    rem = num % 10
    sum = sum * 10 + rem
    num //= 10

print(f"Reverse of {temp} is {sum}")
