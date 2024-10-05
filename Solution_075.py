# Write a Python program to check if a number is a perfect cube.

num = int(input("Enter a number : "))

cube = round(num**(1/3))

if cube**3 == num:
    print(f"{num} is a perfect cube of {cube}")
else:
    print(f"{num} is not a perfect cube")
