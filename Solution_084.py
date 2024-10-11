# Write a Python program to find the first non-repeating character in a string.

str = input("Enter your String : ")
flag = -1

for i in str:
    flag = -1
    for j in str:
        if i == j:
            flag += 1
    if flag == 0:
        print(f"The first non-repeating character is {i}")
        break
