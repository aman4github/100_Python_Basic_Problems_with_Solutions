# Write a Python program to remove all vowels from a string.

str = input("Enter your String : ")
str2 = ""

for i in str:
    if i != "A" and i != "E" and i != "I" and i != "O" and i != "U" and i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        str2 += i

print(f"String after removing all vowel is {str2}")
