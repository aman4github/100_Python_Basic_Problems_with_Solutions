# Write a Python program to reverse a string.

str = input("Enter a String : ")

# Method 1 
for i in range(len(str) - 1, -1, -1):
    print(str[i], end="")

# Method 2 
print() # For one new line
print(str[::-1])