# Write a Python program to check if a number is even or odd.

num = int(input("Enter the number : "))

if num == 0:
    print(f"{num} is nither Odd nor Even")
elif num % 2 == 0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")