# Write a Python program to swap two numbers without using a temporary variable.

num1 = 35
num2 = 97

print(f"Before Swapping num1 = {num1} and num2 = {num2}")

# Method 1 
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After Swapping num1 = {num1} and num2 = {num2}")

# Method 2 

num1 = 35
num2 = 97

num1, num2 = num2, num1

print(f"After Swapping num1 = {num1} and num2 = {num2}")