# Write a Python program to find the greatest common divisor (GCD) of two numbers.

# Method 1 
num1, num2 = 15, 30
lst = []
i = 2

print(f"GCD of {num1} and {num2} = ", end="")

while num1 > 1 and num2 > 1:
    if num1 % i == 0 and num2 % i == 0:
        lst.append(i)
        num1 //= i
        num2 //= i
    else:
        i += 1

gcd_value = 1

for factor in lst:
    gcd_value *= factor

print(gcd_value)

# Method 2 

num1, num2 = 15, 30

gcd = 1

i = 2

print(f"GCD of {num1} and {num2} = ", end="")

while i <= min(num1, num2):
    if num1 % i == 0 and num2 % i == 0:
        gcd *= i
        num1 //= i
        num2 //= i
    else:
        i += 1

print(gcd)

# Method 3 [ Euclidean Algorithm ]

def gcd_fun(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

num1, num2 = 15, 30

print(f"GCD of {num1} and {num2} = {gcd_fun(num1, num2)}")
