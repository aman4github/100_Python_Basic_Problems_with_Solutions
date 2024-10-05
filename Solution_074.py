# Write a Python program to check if a number is a perfect square.
import math

num = int(input("Enter a number : "))

sq = math.sqrt(num)

if sq.is_integer():
    print(f"{num} is a perfect square of {sq}")
else:
    print(f"{num} is not a perfect square")
