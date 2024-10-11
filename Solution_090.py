# Write a Python program to check if a number is a power of three.

num = int(input("Enter the number : "))
temp = num
lst =[]
flag = 0

if num > 0:
    while temp != 1:
        rem = temp % 3
        lst.append(rem)
        temp //= 3
    
    for i in lst:
        if i != 0:
            flag += 1
    if flag == 0:
        print(f"{num} is a power of three")
    else:
        print(f"{num} is not a power of three")
else:
    print(f"{num} is not a power of three")
