# Write a Python program to check if a number is a palindrome.

num = int(input("Enter a Number : "))
sum = 0
temp = num

while temp != 0:
    rem = temp % 10
    sum = sum * 10 + rem
    temp //= 10

if num == sum:
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a Palindrome number")
