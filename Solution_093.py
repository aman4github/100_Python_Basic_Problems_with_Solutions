# Write a Python program to convert a string to uppercase without using the upper() function.

str = input("Enter the String : ")
str2 = ""

for i in str:
    if ord(i) >= 97 and ord(i) <= 122:
        str2 += chr(ord(i) - 32)
    else:
        str2 += i

print(f"{str} in uppercase will be = {str2}")
