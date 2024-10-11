# Write a Python program to check if a string is a valid identifier.
import keyword

str = input("Enter the String : ")

if str.isidentifier() and not keyword.iskeyword(str):
    print(f"{str} is a valid identifier")
else:
    print(f"{str} is not a valid identifier")
    