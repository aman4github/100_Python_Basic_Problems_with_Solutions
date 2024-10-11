# Write a Python program to check if a number is a power of two.

num = int(input("Enter the number : "))

# Method 1 
if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a power of two")
else:
    print(f"{num} is not a power of two")

# Mrthod 2 
temp = num
lst =[]
flag = 0

if temp > 0:
    while temp != 1:
        rem = temp % 2
        lst.append(rem)
        temp //= 2

    for i in lst:
        if i == 1:
            print(f"{num} is not a power of two")
            break
    else:
        print(f"{num} is a power of two")
else:
    print(f"{num} is not a power of two")

