# Write a Python program to find the least common multiple (LCM) of two numbers.

# Method 1 by using GCD 

def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

num1, num2 = 10, 15

print(f"LCM of {num1} and {num2} is {(num1 * num2) // gcd(num1, num2)}")

# Method 2 

num1, num2 = 10, 15
temp_num1, temp_num2 = num1, num2
i = 2
lst = []

while num1 > 1 and num2 > 1:
    if num1 % i == 0 and num2 % i == 0:
        lst.append(i)
        num1 //= i
        num2 //= i
    elif num1 % i == 0:
        num1 //= i
        lst.append(i)
    elif num2 % i == 0:
        num2 //= i
        lst.append(i)
    else:
        i += 1

lcm_factor = 1

for factors in lst:
    lcm_factor *= factors

print(f"LCM of {temp_num1} and {temp_num2} is {lcm_factor}")
