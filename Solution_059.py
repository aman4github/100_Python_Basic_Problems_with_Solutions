# Write a Python program to count the number of uppercase and lowercase letters in a string.

str = input("Enter your string : ")
upper = 0
lower = 0

for i in str:
    if ord(i) >= 97 and ord(i) <= 122:
        lower += 1
    elif ord(i) >= 65 and ord(i) <= 90:
        upper += 1

print(f"Number of Uppercase characters are {upper}\nNumber of Lowercase characters are {lower}")
