# Write a Python program to check if a string is a palindrome.

str = input("Enter a String : ")

flag = 0

for i in range(0, len(str)):
    if str[0] == str[len(str)-1]:
        flag = 0
    else:
        flag += 1

if flag == 0:
    print(f"{str} is a Palindrome String")
else:
    print(f"{str} is not a Palindrome String")
    