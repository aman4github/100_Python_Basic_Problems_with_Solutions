# Write a Python program to generate the Fibonacci sequence.

num1 = 0
num2 = 1

limit = int(input("Enter the limit : "))

print(f"Fibonacci Series - {num1} {num2}", end=" ")

for i in range(1, (limit + 1)):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3
