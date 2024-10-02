# Write a Python program to check if two strings are anagrams.

str1 = input("Enter your 1st string : ")
str2 = input("Enter your 2nd string : ")
flag = 0

if len(str1) == len(str2):
    for i in str1:
        flag = 0
        if str1.count(i) != str2.count(i):
            flag += 1
    if flag == 0:
        print("Yes, the strings are angrams")
    else:
        print("No, the strings are not angrams")
else:
    print("No, the strings are not angrams")
