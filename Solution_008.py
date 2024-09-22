# Write a Python program to check if a number is prime.

num = int(input("Enter a number : "))
flag = 0

for i in range(2, int(num/2)):
    if num % i == 0:
        flag += 1
        break

if flag == 0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")