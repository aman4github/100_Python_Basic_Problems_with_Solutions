# Write a Python program to find the power of a number using recursion.

def power_cal(n, p):
    if n == 0 or n == 1:
        return n
    elif p == 1:
        return n
    else:
        return n * power_cal(n, (p - 1))

num = 5
power = 5

print(power_cal(num, power))
