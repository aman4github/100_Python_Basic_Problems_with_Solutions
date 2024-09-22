# Write a Python program to find the length of a string without using the len() function

str = input("Enter the String : ")
flag = 0

str.lower()
for i in str:
    if ord(i) >= 32 and ord(i) <= 127: # Using ASCII value
        flag += 1
    else:
        break

print(f"Length of the String is {flag}")
