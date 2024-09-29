# Write a Python program to convert a binary number to decimal.

bin_num = 1010110
i = 0
deci = 0
print(f"Decimal of binary num {bin_num} is ", end="")

while bin_num != 0:
    rem = bin_num % 10
    deci += rem * (2**i)
    i += 1
    bin_num //= 10

print(deci)
