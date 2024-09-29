# Write a Python program to convert a decimal number to binary.

num = int(input("Enter a decimal number : "))
binary_lst = []
print(f"Binary of decimal number {num} is ", end="")

while num != 0:
    binary_lst.append((num % 2))
    num //= 2

print(binary_lst[::-1])
