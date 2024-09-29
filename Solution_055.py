# Write a Python program to convert a hexadecimal number to decimal.

hex_num = "5E7"
j = 0
deci = 0

print(f"Decimal of Hexa-Decimal number {hex_num} is ", end="")

for i in hex_num[::-1]:
    if i == "A":
        deci += 10 * (16**j)
    elif i == "B":
        deci += 11 * (16**j)
    elif i == "C":
        deci += 12 * (16**j)
    elif i == "D":
        deci += 13 * (16**j)
    elif i == "E":
        deci += 14 * (16**j)
    elif i == "F":
        deci += 15 * (16**j)
    elif int(i) < 10:
        deci += int(i) * (16**j)
    j += 1

print(deci)
