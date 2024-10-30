# Write a Python program to check if a string contains only digits.

str = input("Enter your string : ")
flag = 0

for i in str:
    if not i.isdigit():
        flag += 1

if flag == 0:
    print("Yes this string contains only digits")
else:
    print("No this string does not contains only digits")

