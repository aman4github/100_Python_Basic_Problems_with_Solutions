# Write a Python program to count the number of consonants in a string.

str = input("Enter your String : ")
flag = 0

for i in str:
    if i != "A" and i != "E" and i != "I" and i != "O" and i != "U" and i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        flag += 1

print(f"Number of consonants in this string is {flag}")
