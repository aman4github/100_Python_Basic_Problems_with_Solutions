# Write a Python program to remove whitespace from a string.

str = input("Enter your string : ")
temp = str # For using the same string in Method 2
str2 = ""

# Method 1 
for i in str:
    if i != " ":
        str2 += i

print(f"New string without space = {str2}")

# Method 2 
print(f"New string after removing all spaces = {str.replace(" ", "")}")
