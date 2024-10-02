# Write a Python program to remove all punctuations from a string.
import string

pun = string.punctuation
flag = 0
str2 = ""
str = input("Enter Your String : ")

for i in str:
    flag = 0
    for j in pun:
        if i == j:
            flag += 1
    if flag == 0:
        str2 += i

print(f"String after removing punctuations {str2}")
