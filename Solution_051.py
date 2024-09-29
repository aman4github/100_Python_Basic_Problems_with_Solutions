# Write a Python program to find the sum of all prime numbers up to a given number.

limit = int(input("Enter the range : "))
flag = 0
total = 0

for i in range(2, limit+1):
    for j in range(2, i):
        if i % j == 0:
            flag += 1
    if flag == 0:
        print(i)
        total += i
    flag = 0
    
print(f"Sum of all prime number within {limit} is {total}")
