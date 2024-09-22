# Write a Python program to count the number of vowels in a string.

str = input("Enter the String : ")
flag = 0

str.lower()
for i in str:
    if (i == "a" or i == "e" or i == "i" or i == "0" or i =="u"):
        flag += 1

if flag == 0:
    print("String does not contains any Vowel")
else:
    print(f"Number or Vowel is {flag}")