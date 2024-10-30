# Write a Python program to count the number of words in a string.

str = input("Enter your string : ")

lst = []
lst.append(str.split())

print(f"The number of words are {len(lst[0])}")
