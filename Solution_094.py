# Write a Python program to convert a string to lowercase without using the lower() function.

str = input("Enter the String : ")
str2 = ""

for i in str:
    if ord(i) >= 65 and ord(i) <= 90:
        str2 += chr(ord(i) + 32)
    else:
        str2 += i

print(f"{str} in lowercase will be = {str2}")
