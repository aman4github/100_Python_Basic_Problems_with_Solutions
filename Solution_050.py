# Write a Python program to find the n-th Fibonacci number using recursion.

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)



n = 6
print(f"Fibonacci Number at n-th position {fibo(n)}")
