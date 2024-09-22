# Write a Python program to find the factorial of a number using recursion.

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

print(f"Factorial of 5 is = {fact(5)}")
