# Write a Python program to find the sum of all numbers in a string.

str = input("Enter your string : ")
sum = 0

for i in str:
    if i.isdigit():
        sum += int(i)
    
print(f"Sum of all digits is {sum}")
