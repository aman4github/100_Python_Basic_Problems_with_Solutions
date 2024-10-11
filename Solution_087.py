# Write a Python program to check if a number is divisible by another number.

num = int(input("Enter a number : "))
flag = 0

for i in range(2, (num//2)+1):
    if num % i == 0:
        flag += 1

if flag == 0:
    print(f"{num} is not divisible by another number")
else:
    print(f"{num} is divisible by another number")