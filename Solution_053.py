# Write a Python program to convert a decimal number to hexadecimal.

num = int(input("Enter a decimal number : "))
hex_lst = []
print(f"Hexa-Decimal of Decimal number {num} is ", end="")


while num != 0:
    rem = num % 16
    if rem < 10:
        hex_lst.append(rem)
    elif rem == 10:
        hex_lst.append("A")
    elif rem == 11:
        hex_lst.append("B")
    elif rem == 12:
        hex_lst.append("C")
    elif rem == 13:
        hex_lst.append("D")
    elif rem == 14:
        hex_lst.append("E")
    elif rem == 15:
        hex_lst.append("F")
    num //= 16
    
print(hex_lst[::-1])
