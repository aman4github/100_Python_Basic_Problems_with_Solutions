# Write a Python program to count the number of prime numbers in a list.

lst = [13, 4, 17, 6, 19, 9, 23]
flag = 0
count = 0

for i in lst:
    flag = 0
    for j in range(2, (i//2)+1):
        if i % j == 0:
            flag += 1
            break
    if flag == 0:
        count += 1

print(f"The number of prime numbers in this list is {count}")
