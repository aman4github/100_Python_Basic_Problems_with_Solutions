# Write a Python program to check if a number is an Armstrong number.

num = int(input("Enter the number : "))

temp = num
flag = 0
sum = 0

while temp != 0:
    temp //= 10
    flag += 1

temp = num

while temp != 0:
    sum += (temp % 10)**flag
    temp //= 10

if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
